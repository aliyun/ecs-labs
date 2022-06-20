# ecs-spot-instance-state-change-notification-fc
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 监听当前地域下所有的抢占式实例的状态，一旦实例处于待回收状态，则将该信息投递到 [消息服务的队列](https://mns.console.aliyun.com/region/cn-hangzhou/queues) 和 [日志服务](https://sls.console.aliyun.com/lognext/profile) 中， 用来记录实例的状态变化。
您可以通过代码订阅 [消息服务的队列](https://mns.console.aliyun.com/region/cn-hangzhou/queues) 进行自定义的中断处理逻辑，或者 查看 [日志服务](https://sls.console.aliyun.com/lognext/profile) 来回溯您实例的历史状态。
## 使用方法:
### GUI 方式
1. 登陆 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将ecs-spot-instance-state-change-notification-fc.yaml粘贴至文本框内
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
```shell
$ aliyun ros CreateStack --StackName ${you-stackName} --TemplateURL  https://raw.githubusercontent.com/${url}/ecs-spot-instance-state-change-notification-fc.yaml
```

## 注意：
每个实例都会触发该ros模版创建的fc, 实例数量多的情况下，消息可能会很多