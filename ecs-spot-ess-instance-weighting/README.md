#ecs-spot-ess-instance-weighting
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 创建[弹性供应组](https://ecs.console.aliyun.com/?spm=5176.2020520101instances.0.0.25f32577TxSTfs#/fleet/region/cn-hangzhou) 并根据实例规格的权重创建满足弹性供应组目标容量的抢占式实例
##使用方法:
###GUI方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将ecs-spot-ess-launch-template.yaml粘贴至文本框内
   ![](docs/ecs-spot-ess-instance-weighting-1.png?raw=true "create ros 1")
4. 设置资源栈名称
5. 选择交换机可用区
6. 设置目标容量，点击创建
   ![](docs/ecs-spot-ess-instance-weighting-2.png?raw=true "create ros 2")
   

###验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-ess-instance-weighting-3.png?raw=true "create ros 3")
2. 查看 [弹性供应组](https://ecs.console.aliyun.com/?spm=5176.2020520101instances.0.0.25f32577TxSTfs#/fleet/region/cn-hangzhou)
3. 查看 弹性供应组 是否为创建出来实例
   ![](docs/ecs-spot-ess-instance-weighting-4.png?raw=true "create ros 2")


### CLI 方式
    //TODO

### 验证
    //TODO

