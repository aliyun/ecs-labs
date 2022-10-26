# spot-interruption-logging-insights
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 监听当前地域下抢占式实例的中断警告，一旦实例处于待回收状态，则将您需要的有关实例的任何详细信息，并默认的 InstanceId、InstanceType 和所有标签等信息 投递到[日志服务](https://sls.console.aliyun.com/lognext/profile) 中， 然后，此信息可用于通过 sls 开发可视化。
## 前提条件：
1. 开通[sls](https://sls.console.aliyun.com/lognext/profile) 服务
## 使用方法:
### GUI方式
1. 登陆 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将spot-interruption-logging-insights.yaml 粘贴至文本框内
   ![](docs/spot-interruption-logging-insights-1.png?raw=true "create ros 1")
4. 设置资源栈名称，点击创建
   ![](docs/spot-interruption-logging-insights-2.png?raw=true "create ros 2")

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/spot-interruption-logging-insights-3.png?raw=true "create ros 3")
2. 当spot实例被回收后查看 [sls日志](https://sls.console.aliyun.com/lognext/profile)
   ![](docs/spot-interruption-logging-insights-4.png?raw=true "create ros 4")
3. 在 查询/分析 输入框内复制以下sql查看同实例规格释放的实例数，您也可以参照日志服务的 [查询与分析](https://help.aliyun.com/document_detail/128135.html) 开发可视化
    ```sql
    $ * | SELECT "InstanceDetails.InstanceType", COUNT(*) as number GROUP BY "InstanceDetails.InstanceType" LIMIT 1000
    ```
   ![](docs/spot-interruption-logging-insights-5.png?raw=true "create ros 4")
   
   ![](docs/spot-interruption-logging-insights-1.gif?raw=true "create ros 5")

### CLI 方式
1. 在本地打开cli或者登陆[云命令行](https://shell.aliyun.com/?spm=5176.21213303.3291411370.3.1dd653c9LowBmg&scm=20140722.S_card@@%E4%BA%A7%E5%93%81@@527485._.ID_card@@%E4%BA%A7%E5%93%81@@527485-RL_cli-OR_ser-V_2-P0_0)
2. 复制粘贴命令, 点击回车键
    ```shell
    $ aliyun ros CreateStack --StackName ecs-spot-ess-launch-template --TemplateURL https://raw.githubusercontent.com/aliyun/ecs-labs/master/spot-interruption-logging-insights/spot-interruption-logging-insights.yaml 
    ```
### 验证
1. 点击回车建后是否返回RequestId和StackId
   ![](docs/spot-interruption-logging-insights-6.png?raw=true "create ros 6")

2. 复制粘贴命令，将${StackId}改为刚返回的StackId 查看资源栈状态 ，若status为CREATE_COMPLETE 表示资源栈创建成功
    ```shell
    $ aliyun ros GetStack --StackId ${StackId}
    ```
   ![](docs/spot-interruption-logging-insights-7.png?raw=true "create ros 7")