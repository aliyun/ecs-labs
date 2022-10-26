import json

from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeTagsRequest import DescribeTagsRequest
from aliyunsdkslb.request.v20140515.RemoveVServerGroupBackendServersRequest import RemoveVServerGroupBackendServersRequest

def handler(event, context):
    creds = context.credentials
    event1 = json.loads(event)
    data = event1.get('data')
    region = context.region
    instance_id = data.get('instanceId')
    credentials = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
    client = AcsClient(region_id=region, credential=credentials)
    try:
        request = DescribeTagsRequest()
        request.set_accept_format('json')
        request.set_ResourceId(instance_id)
        request.set_ResourceType("instance")
        tags = json.loads(client.do_action_with_exception(request))
    except Exception as e:
        print(e)
        print("No action being taken. Unable to describe tags for instance id:", instance_id)
        return
    try:
        request = RemoveVServerGroupBackendServersRequest()
        request.set_accept_format('json')
        for tag in tags['Tags']['Tag']:
            if tag['TagKey'] == 'loadBalancerTargetGroupe':
                request.set_VServerGroupId(tag['TagValue'])
        request.set_BackendServers([
            {
                "ServerId": instance_id,
                "Port": 80
            }
        ])
        removeServerGroupBackendServers = client.do_action_with_exception(request)
        response = client.do_action_with_exception(request)

    except Exception as e:
        print(e)
        print("No action being taken. Unable to deregister targets for instance id:", instance_id)
        return
    print("Spot Instance interruption notice detected. Detaching instance from target:")
    print(instance_id, response, sep=",")
    return