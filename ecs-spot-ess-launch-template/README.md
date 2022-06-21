# ecs-spot-ess-launch-template
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 来快捷地创建抢占式实例
## 使用方法:
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ecs-spot-ess-launch-template.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-ess-launch-template/ecs-spot-ess-launch-template.yaml) 粘贴至文本框内
   ![](docs/ecs-spot-ess-launch-template-1.gif?raw=true "create ros 1")
4. 设置资源栈名称 
5. 选择密钥对,点击创建
   ![](docs/ecs-spot-ess-launch-template-2.gif?raw=true "create ros 2")
   

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-ess-launch-template-1.png?raw=true "create ros 3")
2. 查看 [弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre9.3be916d0v60i3Z#/v3/group/list/cn-hangzhou) 是否创建了两个实例
   ![](docs/ecs-spot-ess-launch-template-2.png?raw=true "create ros 4")
3. 查看 [实例](https://ecs.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre4.3be916d0Kc8eUf#/server/region/cn-hangzhou) 是否为抢占式实例
   ![](docs/ecs-spot-ess-launch-template-3.png?raw=true "create ros 5")
   ![](docs/ecs-spot-ess-launch-template-3.gif?raw=true "create ros 6")

### CLI 方式
1. 在本地打开cli或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 将${user-KeyPairName}改为您的密钥对名称，若没有则[创建密钥对](https://ecs.console.aliyun.com/?spm=5176.13689198.0.0.2c6b2068XsSV7r#/keyPair/region/cn-hangzhou/create?createType=default) 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ecs-spot-ess-launch-template --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/ecs-spot-ess-launch-template/ecs-spot-ess-launch-template.yaml --Parameters.1.ParameterKey KeyPairName --Parameters.1.ParameterValue ${user-KeyPairName}
    ```
    ![](docs/ecs-spot-ess-launch-template-4.gif?raw=true "create ros 7")

### 验证
1. 点击回车建后是否返回RequestId和StackId
   ![](docs/ecs-spot-ess-launch-template-4.png?raw=true "create ros 8")
   
2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看[资源栈状态](https://ros.console.aliyun.com/cn-hangzhou/stacks) ，若status为CREATE_COMPLETE 表示资源栈创建成功
   ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](docs/ecs-spot-ess-launch-template-5.png?raw=true "create ros 9")

3. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看 [弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre9.3be916d0v60i3Z#/v3/group/list/cn-hangzhou) 是否创建了成功
   ```shell
   $ aliyun ros ListStackResources --StackId ${StackId}
   ```
   ![](docs/ecs-spot-ess-launch-template-6.png?raw=true "create ros 10")
   
4. 复制粘贴命令，将${PhysicalResourceId}改为刚返回的PhysicalResourceId 查看伸缩组内 [实例](https://ecs.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre4.3be916d0Kc8eUf#/server/region/cn-hangzhou) 数量是否为2，是否为抢占式实例
   ```shell
   $ aliyun ess DescribeScalingInstances --ScalingGroupId ${PhysicalResourceId}
    ```
   ![](docs/ecs-spot-ess-launch-template-7.png?raw=true "create ros 11")

## 注意：
该模版只能在杭州地域下使用，若要在其他地域使用需要更改模版中的 ZoneId, InstanceType。
ZoneId 为您想要使用地域下的可用区
InstanceType为可用区下再售的实例规格


