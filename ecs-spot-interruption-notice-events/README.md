# ecs-spot-interruption-notice-events
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 在抢占式实例收到中断消息时提前从 [slb负载均衡器](https://help.aliyun.com/document_detail/85931.html?spm=5176.11783163.help.dexternal.777e1eb9OEnvFO)
## 使用方法:
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ecs-spot-interruption-handler.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-interruption-notice-events/ecs-spot-interruption-notice-events.yaml) 粘贴至文本框内  
   ![](docs/ecs-spot-interruption-notice-events-1.png?raw=true "create ros ")
4. 设置资源栈名称
5. 选择vpc
6. 选择交换机主可用区
7. 交换机
8. 选择交换机从可用区
9. 设置消息保存时长
   ![](docs/ecs-spot-interruption-notice-events-2.png?raw=true "create ros ")

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-interruption-notice-events-3.png?raw=true "create ros ")
2. 查看是否创建 [FC函数计算](https://fcnext.console.aliyun.com/overview)
   ![](docs/ecs-spot-interruption-notice-events-4.png?raw=true "create ros ")
3. 查看是否创建 [slb负载均衡器](https://slb.console.aliyun.com/slb/cn-hangzhou/slbs)
   ![](docs/ecs-spot-interruption-notice-events-5.png?raw=true "create ros ")
4. 创建抢占式实例, 并把实例绑定到创建的slb上 
   * 实例需要打上标签 Key: loadBalancerTargetGroup Value: rsp-bxxxxxxxx ,Value值为刚创建的负载均衡器 虚拟服务器组 Id
     ![](docs/ecs-spot-interruption-notice-events-6.png?raw=true "create ros ")

   * 实例绑定slb步骤  
     ![](docs/ecs-spot-interruption-notice-events-7.png?raw=true "create ros ")
     ![](docs/ecs-spot-interruption-notice-events-8.png?raw=true "create ros ")
     ![](docs/ecs-spot-interruption-notice-events-9.png?raw=true "create ros ")
   
   ![](docs/ecs-spot-interruption-notice-events-10.png?raw=true "create ros ")
    
5. 当抢占式实例接收到中断通知后查看slb是否剥离实例
   ![](docs/ecs-spot-interruption-notice-events-11.png?raw=true "create ros ")
### CLI 方式
1. 在本地打开 [cli](https://help.aliyun.com/document_detail/139508.html) 或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ${user-StackName} --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/ecs-spot-interruption-notice-events/ecs-spot-interruption-notice-events.yaml --Parameters.1.ParameterKey MasterVSwitchZoneId --Parameters.1.ParameterValue ${user-MasterVSwitchZoneId}  --Parameters.2.ParameterKey MessageRetentionPeriod --Parameters.2.ParameterValue ${user-MessageRetentionPeriod} --Parameters.3.ParameterKey SlaveVSwitchZoneId --Parameters.3.ParameterValue ${user-SlaveVSwitchZoneId}  --Parameters.4.ParameterKey VPC --Parameters.4.ParameterValue ${user-VPC}  --Parameters.5.ParameterKey VSwitch --Parameters.5.ParameterValue ${user-VSwitch}
    ```
    ![](docs/ecs-spot-interruption-notice-events-12.png?raw=true "create ros ")
   
### 验证
1. 点击回车建后是否返回RequestId和StackId
2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
    ![](docs/ecs-spot-interruption-notice-events-13.png?raw=true "create ros ")
3. 复制粘贴命令，将${StackId}改为刚返回的StackId ,查看是否创建 [FC函数计算](https://fcnext.console.aliyun.com/overview) ,是否创建 [slb负载均衡器](https://slb.console.aliyun.com/slb/cn-hangzhou/slbs)
    ```shell
   $ aliyun ros ListStackResources --StackId ${StackId}
   ```
    ![](docs/ecs-spot-interruption-notice-events-14.png?raw=true "create ros ")
   
## 联系我们
钉钉群号：31407265

