import json

from aliyunsdkess.request.v20140828.DetachInstancesRequest import DetachInstancesRequest
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkcore.client import AcsClient


def handler(event, context):
    creds = context.credentials
    event1 = json.loads(event)
    data = event1.get('data')
    region = context.region
    if event1.get('type') == "ecs:Instance:PreemptibleInstanceInterruption":
        instance_id = data.get('instanceId')
    else:
        instance_id = data.get('resourceId')

    print("Handling spot instance interruption notification for instance {id}".format(id=instance_id))
    ecs = ECS(region, creds)
    interruption_handling_properties = ecs.get_interruption_handling_properties(instance_id)

    # if the instance is tagged as managed and belongs to an Auto Scaling group
    if interruption_handling_properties['managed']:
        if interruption_handling_properties['controller-id'] != '':
            # if it's an Auto Scaling group call detachInstances
            if interruption_handling_properties['controller-type'] == 'auto-scaling-group':
                ecs.detach_instance_from_asg(interruption_handling_properties['controller-id'], instance_id)
                print("INFO: Instance {id} has been successfully detached from {asg_name}".format(
                    id=instance_id, asg_name=interruption_handling_properties['controller-id']))
        else:
            info_message = "No action taken. Instance {id} is not part of an Auto Scaling group.".format(
                id=instance_id)
            print(info_message)
            return (info_message)
    else:
        info_message = "No action taken. Instance {id} is not managed by SpotInterruptionHandler.".format(
            id=instance_id)
        print(info_message)
        return (info_message)

    info_message = "Interruption response actions completed for instance {id} belonging to {controller}".format(
        id=instance_id, controller=interruption_handling_properties['controller-id'])
    print(info_message)
    return (info_message)


class ECS():
    def __init__(self, region, creds):
        credentials = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
        self.client = AcsClient(region_id=region, credential=credentials)

    def describe_instances(self, instance_ids):
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        request.set_InstanceIds(str(instance_ids))
        try:
            response = self.client.do_action_with_exception(request)

            instances = json.loads(response)
            instance = instances.get('Instances').get('Instance')[0]
            print(instance)
            return instance
        except Exception as e:
            print("Unexpected error: %s" % e)
            return

    def get_interruption_handling_properties(self, instance_id):

        # Describe tags for the instance that will be interrupted
        try:
            describe_tags_response = self.describe_instances([instance_id])
            instance_tags = describe_tags_response['Tags']['Tag']
        # except ClientError as e:
        except Exception as e:
            error_message = "Unable to describe tags for instance id: {id}. ".format(id=instance_id)
            print(error_message + str(e))
            # Instance does not exist or cannot be described
            raise e

        interruption_handling_properties = {
            'controller-type': '',
            'controller-id': '',
            'managed': False}

        # Check if instance belongs to an ASG
        for tag in instance_tags:
            if tag['TagKey'] == 'acs:autoscaling:scalingGroupId':
                # Instance belongs to an Auto Scaling group
                interruption_handling_properties['controller-type'] = 'auto-scaling-group'
                interruption_handling_properties['controller-id'] = tag['TagValue']
            elif tag['TagKey'] == 'SpotInterruptionHandler/enabled':
                interruption_handling_properties['managed'] = tag['TagValue'].lower() == 'true'

        return interruption_handling_properties

    def detach_instance_from_asg(self, scaling_group_id, instance_id):
        try:
            detach_instances_request = DetachInstancesRequest()
            detach_instances_request.set_InstanceIds([instance_id])
            detach_instances_request.set_ScalingGroupId(scaling_group_id)
            detach_instances_request.set_DecreaseDesiredCapacity(False)
            response = self.client.do_action_with_exception(detach_instances_request)
            print(response)
        except Exception as e:
            error_message = "Unable to detach instance {id} from AutoScaling Group {asg_name}. ".format(
                id=instance_id, asg_name=scaling_group_id)
            print(error_message + str(e))
            raise e