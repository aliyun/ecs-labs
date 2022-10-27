# ecs-spot-instance-state-change-notification-fc
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 监听当前地域下所有的抢占式实例的状态，一旦实例处于待回收状态，则将该信息投递到 [消息服务的队列](https://mns.console.aliyun.com/region/cn-hangzhou/queues) 和 [日志服务](https://sls.console.aliyun.com/lognext/profile) 中， 用来记录实例的状态变化。
您可以通过代码订阅 [消息服务的队列](https://mns.console.aliyun.com/region/cn-hangzhou/queues) 进行自定义的中断处理逻辑，或者 查看 [日志服务](https://sls.console.aliyun.com/lognext/profile) 来回溯您实例的历史状态。
## 前提条件：
1. 开通[sls](https://sls.console.aliyun.com/lognext/profile) 服务
2. 开通[消息服务MNS](https://mns.console.aliyun.com/)
3. 开通[事件总线](https://eventbridge.console.aliyun.com/overview) 并授权角色
4. 登陆[RAM控制台](https://ram.console.aliyun.com/roles) 创建角色AliyunServiceRoleForEventBridgeSendToFC
   ![](docs/ecs-spot-instance-state-change-notification-fc-5.gif?raw=true "create ros 1")
   
5. 创建角色AliyunServiceRoleForEventBridgeSendToMNS
   ![](docs/ecs-spot-instance-state-change-notification-fc-6.gif?raw=true "create ros 1")

## 使用方法:
### GUI 方式
1. 登陆 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ecs-spot-instance-state-change-notification-fc.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-instance-state-change-notification-fc/ecs-spot-instance-state-change-notification-fc.yaml) 粘贴至文本框内
4. 设置资源栈名称，点击创建
![](docs/ecs-spot-instance-state-change-notification-fc-1.gif?raw=true "create ros 1")

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
![](docs/ecs-spot-instance-state-change-notification-fc-1.png?raw=true "create ros 2")
2. 实例状态发生改变时查看 [sls日志](https://sls.console.aliyun.com/lognext/profile)
![](docs/ecs-spot-instance-state-change-notification-fc-2.png?raw=true "create ros 3")
![](docs/ecs-spot-instance-state-change-notification-fc-2.gif?raw=true "create ros 5")
3. 实例状态发生改变时查看 [队列消息](https://mns.console.aliyun.com/region/cn-hangzhou/queues)
![](docs/ecs-spot-instance-state-change-notification-fc-3.png?raw=true "create ros 4")
![](docs/ecs-spot-instance-state-change-notification-fc-3.gif?raw=true "create ros 6")


### CLI 方式
1. 在本地打开 [cli](https://help.aliyun.com/document_detail/139508.html) 或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ecs-spot-ess-launch-template --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/ecs-spot-instance-state-change-notification-fc/ecs-spot-instance-state-change-notification-fc.yaml
    ```
   ![](docs/ecs-spot-instance-state-change-notification-fc-4.gif?raw=true "create ros 6")
### 验证
1. 点击回车建后是否返回RequestId和StackId
   
   ![](docs/ecs-spot-instance-state-change-notification-fc-4.png?raw=true "create ros 7")
   
2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](docs/ecs-spot-instance-state-change-notification-fc-5.png?raw=true "create ros 8")
   
3. 实例状态发生改变时查看 [sls日志](https://sls.console.aliyun.com/lognext/profile)
   ![](docs/ecs-spot-instance-state-change-notification-fc-2.png?raw=true "create ros 9")
   ![](docs/ecs-spot-instance-state-change-notification-fc-2.gif?raw=true "create ros 10")
4. 实例状态发生改变时查看 [队列消息](https://mns.console.aliyun.com/region/cn-hangzhou/queues)
   ![](docs/ecs-spot-instance-state-change-notification-fc-3.png?raw=true "create ros 11")
   ![](docs/ecs-spot-instance-state-change-notification-fc-3.gif?raw=true "create ros 12")
## 注意：
每个实例都会触发该ros模版创建的fc, 实例数量多的情况下，消息可能会很多
## 联系我们
钉钉群号：31407265