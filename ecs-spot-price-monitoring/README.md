# ecs-spot-price-monitoring-with-fc
此实验用来演示：如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 查询已创建的抢占式实例规格的价格并把信息上传至 [云监控自定义监控](https://cms.console.aliyun.com/custom-monitoring/_all) 中方便查看已创建的抢占式实例价格变化
## 使用方法:
### GUI 方式
1. 登陆 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将ecs-spot-price-monitoring-with-fc.yaml粘贴至文本框内
   ![](docs/ecs-spot-price-monitoring-with-fc-1.gif?raw=true "create ros 1")
4. 设置资源栈名称
5. 设置定时任务执行结束时间，点击创建
    ![](docs/ecs-spot-price-monitoring-with-fc-2.gif?raw=true "create ros 2")

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-price-monitoring-with-fc-1.png?raw=true "create ros 4")

2. 创建成功后登陆 [云监控](https://cms.console.aliyun.com/custom-monitoring/_all) 点击自定义监控查看spot实例计费折线图
  ![](docs/ecs-spot-price-monitoring-with-fc-2.png?raw=true "create ros 4")
  ![](docs/ecs-spot-price-monitoring-with-fc-3.gif?raw=true "create ros 1")
### CLI 方式  
```shell
$ aliyun ros CreateStack --StackName ${you-stackName} --TemplateURL  https://raw.githubusercontent.com/${url}/ecs-spot-price-monitoring-with-fc.yaml
```