# ecs-spot-interruption-handler
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 在抢占式实例收到中断消息时提前从 [弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre9.3be916d0v60i3Z#/v3/welcome/) 剥离
## 使用方法:
### 使用前提
使用 ess-sample 模版创建出弹性伸缩组且生产出抢占式实例
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ecs-spot-interruption-handler.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-interruption-handler/ecs-spot-interruption-handler.yaml) 粘贴至文本框内  
   ![](docs/ecs-spot-interruption-handler-1.png?raw=true "create ros ")
4.设置资源栈名称，点击创建
   ![](docs/ecs-spot-interruption-handler-2.png?raw=true "create ros ")
   ![](docs/ecs-spot-interruption-handler-1.gif "create ros ")
   
### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-interruption-handler-3.png?raw=true "create ros ")
2. 查看是否创建 [FC函数计算](https://fcnext.console.aliyun.com/overview)
   ![](docs/ecs-spot-interruption-handler-4.png?raw=true "create ros ")
3. 当抢占式实例接收到中断通知后查看弹性伸缩组是否剥离实例
   ![](docs/ecs-spot-interruption-handler-5.png?raw=true "create ros ")

### CLI 方式
1. 在本地打开 [cli](https://help.aliyun.com/document_detail/139508.html) 或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ${user-StackName} --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/ecs-spot-interruption-handler/ecs-spot-interruption-handler.yaml
    ```
   ![](docs/ecs-spot-interruption-handler-8.png?raw=true "create ros ")

### 验证
1. 点击回车建后是否返回RequestId和StackId
   ![](docs/ecs-spot-interruption-handler-9.png?raw=true "create ros ")
2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](docs/ecs-spot-interruption-handler-10.png?raw=true "create ros ")
3. 复制粘贴命令，将${StackId}改为刚返回的StackId, 查看是否创建 [FC函数计算](https://fcnext.console.aliyun.com/overview)
    ```shell
   $ aliyun ros ListStackResources --StackId ${StackId}
   ```
   ![](docs/ecs-spot-interruption-handler-11.png?raw=true "create ros ")
   

## 联系我们
钉钉群号：31407265

