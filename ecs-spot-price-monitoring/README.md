# ecs-spot-price-monitoring-with-fc
此实验用来演示：如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 每隔一小时查询已创建的抢占式实例规格的价格并把信息上传至 [云监控自定义监控](https://cms.console.aliyun.com/custom-monitoring/_all) 中方便查看已创建的抢占式实例价格变化
## 前提条件：
1. 开通[sls](https://sls.console.aliyun.com/lognext/profile) 服务
2. 登陆[RAM角色管理控制台](https://ram.console.aliyun.com/roles?spm=a2c4g.11186623.0.0.481c703byBWQLH) 创建[oos扮演的角色](https://help.aliyun.com/document_detail/120810.html?spm=5176.202021321.automation.5.4b6e67e7rObI6N) OOSServiceRole
   ![](docs/ecs-spot-price-monitoring-with-fc-5.gif?raw=true "create ros 1")
3. 给OOSServiceRole角色添加AliyunFCInvocationAccess权限
   ![](docs/ecs-spot-price-monitoring-with-fc-6.gif?raw=true "create ros 1")
## 使用方法:
### GUI 方式
1. 登陆 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ecs-spot-price-monitoring-with-fc.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-price-monitoring/ecs-spot-price-monitoring-with-fc.yaml) 粘贴至文本框内
   ![](docs/ecs-spot-price-monitoring-with-fc-1.gif?raw=true "create ros 1")
4. 设置资源栈名称
5. 设置定时任务执行结束时间，点击创建
    ![](docs/ecs-spot-price-monitoring-with-fc-2.gif?raw=true "create ros 2")

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-price-monitoring-with-fc-1.png?raw=true "create ros 3")

2. 创建成功后隔一小时登陆 [云监控](https://cms.console.aliyun.com/custom-monitoring/_all) 点击自定义监控查看spot实例计费折线图
  ![](docs/ecs-spot-price-monitoring-with-fc-2.png?raw=true "create ros 4")
  ![](docs/ecs-spot-price-monitoring-with-fc-3.gif?raw=true "create ros 5")
### CLI 方式  
1. 在本地打开 [cli](https://help.aliyun.com/document_detail/139508.html) 或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 将${endDate}改为您的希望定时任务结束的事件如 2022-06-22T01:51:38Z ， 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ecs-spot-price-monitoring-with-fc --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/ecs-spot-price-monitoring/ecs-spot-price-monitoring-with-fc.yaml --Parameters.1.ParameterKey OOSExecutionEndDate --Parameters.1.ParameterValue ${endDate}
    ```
    ![](docs/ecs-spot-price-monitoring-with-fc-4.gif?raw=true "create ros 6")
### 验证
1. 点击回车建后是否返回RequestId和StackId
   
    ![](docs/ecs-spot-price-monitoring-with-fc-4.png?raw=true "create ros 7")
   
2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](docs/ecs-spot-price-monitoring-with-fc-5.png?raw=true "create ros 8")

2. 创建成功后隔一小时登陆 [云监控](https://cms.console.aliyun.com/custom-monitoring/_all) 点击自定义监控查看spot实例计费折线图
   ![](docs/ecs-spot-price-monitoring-with-fc-2.png?raw=true "create ros 9")
   ![](docs/ecs-spot-price-monitoring-with-fc-3.gif?raw=true "create ros 10")
   
## FAQ
1. 如何更改每隔多久查询已创建的抢占式实例规格的价格？
   答：更改yaml中的cron表达式。如果设置oos触发的时间正好为每小时的前10分钟，由于该时段价格还未产出所以数据不会上传致云监控中
   
## 联系我们
钉钉群号：31407265