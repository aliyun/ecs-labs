# ecs-spot-apg-launch
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 使用指定 [启动模版](https://help.aliyun.com/document_detail/73916.html?spm=a2c4g.11186623.0.0.7f8651d3NdvxB5) 的 [弹性供应](https://help.aliyun.com/document_detail/120020.html) 快速快速部署抢占式实例集群
## 使用方法:
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将[ecs-spot-apg-launch-templates.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-spot-apg-launch-templates/ecs-spot-apg-launch-templates.yaml) 粘贴至文本框内
   ![](docs/ecs-spot-apg-launch-templates-1.png?raw=true "create ros 1")
4. 填写资源栈名称
5. 选择密钥对
6. 填写总目标容量, 点击创建
   ![](docs/ecs-spot-apg-launch-templates-2.png?raw=true "create ros 1")
   

### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-spot-apg-launch-templates-3.png?raw=true "create ros 2")
   
2. 查看是否创建 [启动模版](https://ecs.console.aliyun.com/?spm=5176.13689198.0.0.46ed2068NfQYJe#/launchTemplate/region/cn-hangzhou)
    
   ![](docs/ecs-spot-apg-launch-templates-4.png?raw=true "create ros 3")
   ![](docs/ecs-spot-apg-launch-templates-5.png?raw=true "create ros 4")
   
3. 查看是否创建 [弹性供应组](https://ecs.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre0.3be916d0ducF6T#/fleet/region/cn-hangzhou)
   
   ![](docs/ecs-spot-apg-launch-templates-6.png?raw=true "create ros 5")
   ![](docs/ecs-spot-apg-launch-templates-7.png?raw=true "create ros 6")
   
4. 查看弹性供应组是创建的抢占式实例数是否等于创建资源栈时填写的总目标容量数
   ![](docs/ecs-spot-apg-launch-templates-8.png?raw=true "create ros 7")

### CLI 方式
    //TODO

### 验证
    //TODO
