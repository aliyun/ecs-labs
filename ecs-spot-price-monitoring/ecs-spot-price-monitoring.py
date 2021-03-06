import datetime
import json
import time

import pytz
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeSpotPriceHistoryRequest import DescribeSpotPriceHistoryRequest
from aliyunsdkecs.request.v20140526.AddTagsRequest import AddTagsRequest
from aliyunsdkcms.request.v20190101.PutCustomMetricRequest import PutCustomMetricRequest


def handler(event, context):
    print('Loading ecs-spot-price-monitoring function.')
    start = int(round(time.time() * 1000))
    ecs = ECS(context)
    instance_list = ecs.describe_instances()
    instance_map = get_instance_map(instance_list)
    keys = instance_map.keys()
    for key in keys:
        k = eval(key)
        price = ecs.get_latest_price(k)
        if price is None:
            continue
        timestamp = price[-1]['Timestamp']
        now = utc0_to_utc8(timestamp)
        print(start - now)
        if 600000 < start - now < 4200000:
            instances = instance_map.get(key)
            ecs.batch_put_instance_metric(instances, price, start)
        else:
            print('当前时价格还未产出')
    end = int(round(time.time() * 1000))
    print('Function ecs-spot-price-monitoring complete. cost: ', end - start)
    return ('complete')

class ECS():
    def __init__(self, context):
        region = context.region
        creds = context.credentials
        credentials = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
        self.client = AcsClient(region_id=region, credential=credentials)

        # 查询当前地域下所有的spot实例
    def describe_instances(self):
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        request.set_Status('Running')
        request.set_Tags([{"Key": "acs:ecs:payType", "value": "spot"}])
        request.set_PageSize(1)
        response = self.client.do_action_with_exception(request)
        res = json.loads(response)
        instance_list = res['Instances']['Instance']
        while (len(res['NextToken']) != 0):
            request.set_NextToken(res['NextToken'])
            request.set_MaxResults(100)
            response1 = self.client.do_action_with_exception(request)
            res = json.loads(response1)
            instance_list.extend(res['Instances']['Instance'])
        return instance_list

    def get_latest_price(self, k):
        request = DescribeSpotPriceHistoryRequest()
        request.set_accept_format('json')
        request.set_InstanceType(k.get('InstanceType'))
        request.set_ZoneId(k.get('ZoneId'))
        request.set_NetworkType("vpc")
        response = self.client.do_action_with_exception(request)
        spotprices = json.loads(response)
        price = spotprices.get('SpotPrices')['SpotPriceType']
        return price

    def batch_put_instance_metric(self, instances, price, now):
        for instance in instances:
            self.put_instance_metric(instance, price, now)

    def put_instance_metric(self, instance, price, now):
        self.add_tags(instance, price)
        tag_keys = {}
        tags = instance.get('Tags')['Tag']
        for t in tags:
            tag_keys[t['TagKey']] = t['TagValue']
        self.put_metric(tag_keys, instance, price, now)

    def put_metric(self, tag_keys, instance, price, now):
        if 'acs:ecs:apgId' in tag_keys.keys():
            dimensions = str({"apgId": tag_keys.get('acs:ecs:apgId')})
            dimensions1 = str({"apgId": tag_keys.get('acs:ecs:apgId'), "InstanceId": instance.get('InstanceId')})
            try:
                self.put_custom_metric(now, price, dimensions)
                self.put_custom_metric(now, price, dimensions1)
            except:
                print('Unable to put custom metric for InstanceId:', instance.get('InstanceId'))
        else:
            dimensions = str({"InstanceId": instance.get('InstanceId')})
            try:
                self.put_custom_metric(now, price, dimensions)
            except Exception as e:
                print(e)
                print('Unable to put custom metric for InstanceId:', instance.get('InstanceId'))

    def put_custom_metric(self, now, price, dimensions):
        request = PutCustomMetricRequest()
        request.set_accept_format('json')
        request.set_MetricLists([{"Type": "0", "MetricName": "Hourly Price", "Time": now,
                                  "GroupId": "0", "Values": str({"value": price[-1]['SpotPrice']}),
                                  "Dimensions": dimensions}])
        response = self.client.do_action_with_exception(request)
        print(response)

    def add_tags(self, instance, price):
        print("start utCustomMetric for instanceId: " + instance.get('InstanceId'))
        request = AddTagsRequest()
        request.set_accept_format('json')
        request.set_ResourceType("instance")
        request.set_Tags([{"Key": "ECS Spot Market Price", "value": str(price[-1]['SpotPrice'])},
                          {"Key": "ECS Spot Bid Price", "value": str(instance['SpotPriceLimit'])}])
        request.set_ResourceId(instance.get('InstanceId'))
        try:
            response =self.client.do_action_with_exception(request)
        except:
            print('Unable to create tag for InstanceId:', instance.get('InstanceId'))


# 获得一个以实例规格+可用区为key，实例详细信息集合为value的map
def get_instance_map(instance_list):
    instance_map = {}
    for instance in instance_list:
        key = str({'InstanceType': instance.get('InstanceType'), 'ZoneId': instance.get('ZoneId')})
        if instance_map.get(key) is None:
            instance_map[key] = [instance]
        else:
            value = instance_map.get(key)
            value.append(instance)
    return instance_map

def utc0_to_utc8(timestamp):
    tz = pytz.timezone('Asia/Shanghai')
    utc_time = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    now = round(utc_time.replace(tzinfo=pytz.utc).astimezone(tz).timestamp() * 1000)
    return now