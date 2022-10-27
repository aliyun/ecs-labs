# ecs-spot-ess-launch-template
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 创建ess弹性伸缩组, 并创建slb负载均衡器
## 使用方法:
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ess-sample.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-interruption-handler/ess-sample/ess-sample.yaml) 粘贴至文本框内
   ![](/ecs-spot-interruption-handler/docs/ess-sample-1.png "create ros 4")
4. 设置资源栈名称
5. 选择vpc
6. 选择负载均衡的主/从 可用区
   ![](/ecs-spot-interruption-handler/docs/ess-sample-2.png)
7. 选择交换机
8. 选择安全组
9. 选择实例规格
    ![](/ecs-spot-interruption-handler/docs/ess-sample-3.png)

10. 选择系统盘类型
11. 选择负载均衡规格
12. 选择密钥对，点击创建
    ![](/ecs-spot-interruption-handler/docs/ess-sample-4.png)

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](/ecs-spot-interruption-handler/docs/ess-sample-5.png "create ros 3")
2. 查看是否创建出一个[弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre9.3be916d0v60i3Z#/v3/group/list/cn-hangzhou)
   ![](/ecs-spot-interruption-handler/docs/ess-sample-6.png "create ros 4")
3. 弹性伸缩组内是否生产出两个实例
   ![](/ecs-spot-interruption-handler/docs/ess-sample-7.png "create ros 4")

### CLI 方式
1. 在本地打开 [cli](https://help.aliyun.com/document_detail/139508.html) 或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ${user-StackName} --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/ecs-spot-interruption-handler/ess-sample/ess-sample.yaml --Parameters.1.ParameterKey InstanceType --Parameters.1.ParameterValue ${user-InstanceType} --Parameters.2.ParameterKey KeyPairName --Parameters.2.ParameterValue ${user-KeyPairName} --Parameters.3.ParameterKey LoadBalancerSpec --Parameters.3.ParameterValue ${user-LoadBalancerSpec} --Parameters.4.ParameterKey SecurityGroup --Parameters.4.ParameterValue ${user-SecurityGroup} --Parameters.5.ParameterKey SlaveVSwitchZoneId --Parameters.5.ParameterValue ${user-SlaveVSwitchZoneId} --Parameters.6.ParameterKey SystemDiskCategory --Parameters.6.ParameterValue ${user-SystemDiskCategory} --Parameters.7.ParameterKey VPC --Parameters.7.ParameterValue ${user-VPC} --Parameters.8.ParameterKey VSwitch --Parameters.8.ParameterValue ${user-VSwitch} --Parameters.9.ParameterKey VSwitchZoneId --Parameters.9.ParameterValue ${user-VSwitchZoneId}
    ```
   ![](/ecs-spot-interruption-handler/docs/ess-sample-8.png "create ros 4")

### 验证
1. 点击回车建后是否返回RequestId和StackId
   ![](/ecs-spot-interruption-handler/docs/ess-sample-9.png?raw=true "create ros ")
2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](/ecs-spot-interruption-handler/docs/ess-sample-10.png?raw=true "create ros ")
  
3. 复制粘贴命令，将${StackId}改为刚返回的StackId, 查看是否创建出一个[弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre9.3be916d0v60i3Z#/v3/group/list/cn-hangzhou)
    ```shell
   $ aliyun ros ListStackResources --StackId ${StackId}
   ```
   ![](/ecs-spot-interruption-handler/docs/ess-sample-11.png?raw=true "create ros ")
   
4. 4. 复制粘贴命令，将${PhysicalResourceId}改为刚返回的PhysicalResourceId 查看伸缩组内 [实例](https://ecs.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre4.3be916d0Kc8eUf#/server/region/cn-hangzhou) 数量是否为2，是否为抢占式实例
    ```shell
    $ aliyun ess DescribeScalingInstances --ScalingGroupId ${PhysicalResourceId}
    ```
   ![](/ecs-spot-interruption-handler/docs/ess-sample-12.png?raw=true "create ros ")

## 联系我们
钉钉群号：31407265

