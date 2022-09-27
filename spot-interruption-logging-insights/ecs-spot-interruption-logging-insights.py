from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyun.log import LogClient, PutLogsRequest, LogItem, IndexConfig
import json
import time

index_detail = {"ttl":7,"log_reduce":False,"line":{"caseSensitive":False,"chn":False,
                                                   "token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&",
                                                            "<",">","/",":","\n","\t","\r"]},
                "keys":{"instanceId":{"type":"text","doc_value":True,"alias":"","caseSensitive":False,"chn":False,
                                      "token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">","/",
                                               ":","\n","\t","\r"]},
                        "regionId":{"type":"text","doc_value":True,"alias":"","caseSensitive":False,"chn":False,
                                    "token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">","/",
                                             ":","\n","\t","\r"]},
                        "instanceType":{"type":"text","doc_value":True,"alias":"","caseSensitive":False,"chn":False,
                                        "token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">",
                                                 "/",":","\n","\t","\r"]},
                        "zoneId":{"type":"text","doc_value":True,"alias":"","caseSensitive":False,"chn":False,
                                  "token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">","/",":",
                                           "\n","\t","\r"]},
                        "aliUid":{"type":"long","doc_value":True,"alias":""},
                        "time":{"type":"text","doc_value":True,"alias":"","caseSensitive":False,"chn":False,
                                "token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">","/",":",
                                         "\n","\t","\r"]}}}

logstore_name = 'spot-interruption-logs'

def handler(event, context):
    print('Loading spot-interruption-logging-insights function.')
    region = context.region
    creds = context.credentials
    event1 = json.loads(event)
    data = event1.get('data')
    print(data)
    instanceId = data.get('instanceId')
    instance_id = [instanceId]
    ecs = ECS(region, creds)
    instance = ecs.describe_instances(instance_id)
    log = LOG(region, creds)
    project_name = log.get_project()
    b = log.exist_index(project_name)
    if b:
        log.create_index(project_name)
        time.sleep(60 * 2)
    print("ready to put logs for %s" % logstore_name)

    log.put_logs(instance, project_name, event)

class ECS():
    def __init__(self, region, creds):
        credentials = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
        self.client = AcsClient(region_id=region, credential=credentials)

    def describe_instances(self, instance_id):
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        request.set_InstanceIds(str(instance_id))
        try:
            response = self.client.do_action_with_exception(request)
            instances = json.loads(response)
            instance = instances.get('Instances').get('Instance')[0]
            print(instance)
            return instance
        except Exception as e:
            print("Unexpected error: %s" % e)
            return

class LOG():
    def __init__(self, region, creds):
        endpoint = region + ".log.aliyuncs.com"
        self.log_client = LogClient(endpoint, creds.access_key_id, creds.access_key_secret, creds.security_token)

    def get_project(self):
        response = self.log_client.list_project(size=-1)
        projects = response.get_projects()
        for project in projects:
            if project.get('description') == logstore_name:
                project_name = project.get('projectName')
        return project_name

    #判读日志库有无索引，没有返回true，有返回false
    def exist_index(self, project_name):
        try:
            self.log_client.get_index_config(project_name, logstore_name)
        except Exception:
            return True
        return False

    def create_index(self, project_name):
        index_config = IndexConfig()
        index_config.from_json(index_detail)
        self.log_client.create_index(project_name, logstore_name, index_config)

    def put_logs(self, instance, project_name, event):
        log_group = []
        log_item = LogItem()
        event1 = json.loads(event)
        contents = [
            ('Event', event),
            ('aliUid', event1['aliyunaccountid']),
            ('instanceType', instance['InstanceType']),
            ('instanceId', instance['InstanceId']),
            ('regionId',  instance['RegionId']),
            ('zoneId',  instance['ZoneId']),
            ('time', event1['time'])
            ]

        log_item.set_contents(contents)
        log_group.append(log_item)
        request = PutLogsRequest(project_name, logstore_name, "", "", log_group, compress=False)
        self.log_client.put_logs(request)

