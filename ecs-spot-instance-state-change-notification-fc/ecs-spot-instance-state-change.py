# -*- coding: utf-8 -*-
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

def handler(event, context):
    creds = context.credentials
    event1 = json.loads(event)
    data = event1.get('data')
    region = context.region
    if event1.get('type') == "ecs:Instance:PreemptibleInstanceInterruption":
        instanceId = data.get('instanceId')
        instanceState = data.get('action')
    else:
        instanceId = data.get('resourceId')
        instanceState = data.get('state')
    instance = [instanceId]
    credentials = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
    client = AcsClient(region_id=region, credential=credentials)
    request = DescribeInstancesRequest()
    request.set_accept_format('json')
    request.set_InstanceIds(str(instance))
    try:
        response = client.do_action_with_exception(request)
    except:
        print("Unable to describe instance ID:", instanceId)
    Instances = json.loads(response)
    if Instances['Instances'].get('Instance'):
        print("Spot Instance found:", instanceId, "State:", instanceState)
    else:
        print("Spot Instance NOT found - skipping", instanceId, "State:", instanceState)
    return