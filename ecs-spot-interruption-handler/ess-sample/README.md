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
    //TODO

### 验证
    //TODO
  

## 联系我们
钉钉群号：31407265

