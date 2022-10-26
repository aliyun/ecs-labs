# aliyun-ack-nodegroup-with-spot
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 来快捷地为ACK创建一个按量节点池，一个抢占式节点池

## 使用方法:
### GUI方式
1. 登陆 资源编排[ROS控制台](https://rosnext.console.aliyun.com/cn-hangzhou/stacks)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将ack-nodegroup-with-spot.yaml 粘贴至文本框内
   ![](docs/ack-nodegroup-with-spot-1.gif?raw=true "create ros 1")
4. 填写参数,点击创建
   ![](docs/ack-nodegroup-with-spot-2.gif?raw=true "create ros 2")
   ![](docs/ack-nodegroup-with-spot-3.gif?raw=true "create ros 3")

### 验证
1. 验证资源栈是否创建成功
   ![](docs/ack-nodegroup-with-spot-1.png?raw=true "create ros 4")
2. 验证目标ack集群是否创建出一个按量弹性伸缩的节点池，一个抢占式弹性伸缩的节点池
   ![](docs/ack-nodegroup-with-spot-4.gif?raw=true "create ros 5")
   ![](docs/ack-nodegroup-with-spot-2.png?raw=true "create ros 6")
3. 验证是否创建出两个按量节点,两个抢占式节点
   ![](docs/ack-nodegroup-with-spot-3.png?raw=true "create ros 7")

### CLI 方式
1. 在本地打开cli或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ecs-spot-ess-launch-template --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/aliyun-ack-nodegroup-with-spot/ack-nodegroup-with-spot.yaml --Parameters.1.ParameterKey ClusterId --Parameters.1.ParameterValue ${clusterId} --Parameters.2.ParameterKey PostPaidInstanceType --Parameters.2.ParameterValue ${instanceType} --Parameters.3.ParameterKey PostPaidKeyPairName --Parameters.3.ParameterValue ${keyPairName} --Parameters.4.ParameterKey PostPaidMaxInstances --Parameters.4.ParameterValue {maxInstances} --Parameters.5.ParameterKey PostPaidMinInstances --Parameters.5.ParameterValue {minInstances} --Parameters.6.ParameterKey PostPaidSystemDiskCategory --Parameters.6.ParameterValue ${systemDiskCategory} --Parameters.7.ParameterKey PostPaidSystemDiskSize --Parameters.7.ParameterValue ${systemDiskSize} --Parameters.8.ParameterKey SpotInstanceType --Parameters.8.ParameterValue ${instanceType} --Parameters.9.ParameterKey SpotKeyPairName --Parameters.9.ParameterValue ${keyPairName} --Parameters.10.ParameterKey SpotMaxInstances --Parameters.10.ParameterValue ${maxInstances} --Parameters.11.ParameterKey SpotMinInstances --Parameters.11.ParameterValue ${minInstances} --Parameters.12.ParameterKey SpotSystemDiskCategory --Parameters.12.ParameterValue ${systemDiskCategory} --Parameters.13.ParameterKey SpotSystemDiskSize --Parameters.13.ParameterValue ${systemDiskSize} --Parameters.14.ParameterKey VSwitch --Parameters.14.ParameterValue ${VSwitch} --Parameters.15.ParameterKey VSwitchZoneId --Parameters.15.ParameterValue ${zoneId}
    ```
### 验证
1. 点击回车建后是否返回RequestId和StackId
   ![](docs/ack-nodegroup-with-spot-4.png?raw=true "create ros 8")

2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](docs/ack-nodegroup-with-spot-5.png?raw=true "create ros 9")
3. 验证目标ack集群是否创建出一个按量弹性伸缩的节点池，一个抢占式弹性伸缩的节点池
   ![](docs/ack-nodegroup-with-spot-4.gif?raw=true "create ros 10")
   ![](docs/ack-nodegroup-with-spot-2.png?raw=true "create ros 11")
4. 验证是否创建出两个按量节点,两个抢占式节点
   ![](docs/ack-nodegroup-with-spot-3.png?raw=true "create ros 12")
    
