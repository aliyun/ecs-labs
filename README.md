# Alibaba Cloud Ecs Labs Project - 阿里云弹性计算最佳实践项目

Alibaba Cloud Ecs labs is a collection of code examples and scripts that illustrates some of the best practices in using Alibaba Cloud ECS Instances. e.g.,Preemptive Instance best practices

阿里云Ecs-Labs是关于阿里云弹性计算最佳实践代码和脚本样例，如：抢占式实例最佳实践

## GitHub代码实验室&工具包

* ### [aliyun-ack-nodegroup-with-spot](https://github.com/aliyun/ecs-labs/tree/master/aliyun-ack-nodegroup-with-spot)
    此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 来快捷地为ACK创建一个按量节点池，一个抢占式节点池

* ### [aliyun-ask-nodegroup-with-spot](https://github.com/aliyun/ecs-labs/tree/master/aliyun-ask-nodegroup-with-spot)
    ASK集群中的Pod基于阿里云弹性容器实例ECI运行在安全隔离的容器运行环境中，您可以使用抢占式实例，从而降低部分场景下使用ECI实例的成本

* ### [ecs-spot-ess-launch-template](https://github.com/aliyun/ecs-labs/tree/master/ecs-spot-ess-launch-template)
    此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 来快捷地创建抢占式实例

* ### [ecs-spot-instance-state-change-notification-fc](https://github.com/aliyun/ecs-labs/tree/master/ecs-spot-instance-state-change-notification-fc)
    此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 监听当前地域下所有的抢占式实例的状态，一旦实例处于待回收状态，则将该信息投递到 [消息服务的队列](https://mns.console.aliyun.com/region/cn-hangzhou/queues) 和 [日志服务](https://sls.console.aliyun.com/lognext/profile) 中， 用来记录实例的状态变化。

* ### [ecs-spot-interruption-handler](https://github.com/aliyun/ecs-labs/tree/master/ecs-spot-interruption-handler)
    此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 在抢占式实例收到中断消息时提前从 [弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre9.3be916d0v60i3Z#/v3/welcome/) 剥离

* ### [ecs-spot-interruption-notice-events](https://github.com/aliyun/ecs-labs/tree/master/ecs-spot-interruption-notice-events)
    此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 在抢占式实例收到中断消息时提前从 [slb负载均衡器](https://help.aliyun.com/document_detail/85931.html?spm=5176.11783163.help.dexternal.777e1eb9OEnvFO)

* ### [ecs-spot-price-monitoring](https://github.com/aliyun/ecs-labs/tree/master/ecs-spot-price-monitoring)
    此实验用来演示：如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 每隔一小时查询已创建的抢占式实例规格的价格并把信息上传至 [云监控自定义监控](https://cms.console.aliyun.com/custom-monitoring/_all) 中方便查看已创建的抢占式实例价格变化
* ### [spot-interruption-logging-insights](https://github.com/aliyun/ecs-labs/tree/master/spot-interruption-logging-insights)
    此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks) 监听当前地域下抢占式实例的中断警告，一旦实例处于待回收状态，则将您需要的有关实例的任何详细信息，并默认的 InstanceId、InstanceType 和所有标签等信息 投递到[日志服务](https://sls.console.aliyun.com/lognext/profile) 中， 然后，此信息可用于通过 sls 开发可视化。

## Contribute & Reporting bugs - 贡献代码&报告代码缺陷
You can open issues if you want to contribute to this project or report bugs.

如果你想帮助此项目更加完善，你可以通过创建issues的方式来提供意见或者报告代码缺陷
