# ecs-spot-ess-launch-template
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 来快捷地创建抢占式实例
## 使用方法:
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 点击创建资源栈，选择使用新资源
3. 选择yaml将ecs-spot-ess-launch-template.yaml粘贴至文本框内
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

```shell
$ aliyun ros CreateStack --StackName ${you-stackName} --TemplateURL  https://raw.githubusercontent.com/${url}/ecs-spot-ess-launch-template.yaml
```


## 注意：
该模版只能在杭州地域下使用，若要在其他地域使用需要更改模版中的 ZoneId, InstanceType。
ZoneId 为您想要使用地域下的可用区
InstanceType为可用区下再售的实例规格


