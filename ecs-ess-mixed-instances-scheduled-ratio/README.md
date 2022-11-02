# ecs-ess-mixed-instances-scheduled-ratio
此实验用来演示: 如何通过 [ROS模板](https://ros.console.aliyun.com/cn-hangzhou/stacks), 使用 [MNS主题](https://mns.console.aliyun.com/region/cn-hangzhou/topics) 调整 [弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.2020520101fleet.203.dess.617d4df57dewWa#/v3/group/list/cn-hangzhou) 按量示例和抢占式示例比例

## 模版使用到的产品
* [弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.2020520101fleet.203.dess.617d4df57dewWa#/v3/group/list/cn-hangzhou)
* [FC函数计算](https://fcnext.console.aliyun.com/cn-hangzhou/services)
* [MNS主题](https://mns.console.aliyun.com/region/cn-hangzhou/topics)
* [抢占式实例](https://help.aliyun.com/document_detail/52088.html)
* [启动模版](https://help.aliyun.com/document_detail/73916.html)

## 使用方法:
### GUI 方式
1. 登陆杭州地域 [资源编排ROS控制台](https://ros.console.aliyun.com/cn-hangzhou/welcome)
2. 选择我的模版点击, 创建模版
   
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-1.png?raw=true "create ros 1")
3. 将 [ecs-ess-mixed-instances-scheduled-ratio.yaml](https://github.com/aliyun/ecs-labs/blob/master/ecs-ess-mixed-instances-scheduled-ratio/ecs-ess-mixed-instances-scheduled-ratio.yaml) 粘贴至文本框内, 点击保存模版,选择保存为我的模版
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-2.png?raw=true "create ros 2")
4. 设置模版名称,点击确定
   
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-3.png?raw=true "create ros 3")
5. 点击创建栈
   
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-4.png?raw=true "create ros 4")
6. 填写资源栈名称
7. 选择vpc
8. 选择可用区
9. 选择交换机
10. 选择安全组
11. 填写镜像ID
    ![](docs/ecs-ess-mixed-instances-scheduled-ratio-5.png?raw=true "create ros 5")
    
12. 选择实例规格
    
    ![](docs/ecs-ess-mixed-instances-scheduled-ratio-6.png?raw=true "create ros 6")

13. 选择系统盘类型
14. 填写伸缩组内实例最小数
15. 填写伸缩组内实例最大数
16. 填写伸缩组内可用实例数
17. 填写伸缩组按量占比, 点击创建
    ![](docs/ecs-ess-mixed-instances-scheduled-ratio-7.png?raw=true "create ros 7")
    
### 验证
1. 查看 [资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks) 是否创建成功
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-8.png?raw=true "create ros 8")
   
2. 查看[弹性伸缩组](https://essnew.console.aliyun.com/?spm=5176.2020520101fleet.203.dess.617d4df57dewWa#/v3/group/list/cn-hangzhou) 是否创建成功, 伸缩组内是否创建出与创建资源栈时填写的最小实例数相同数量的实例
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-9.png?raw=true "create ros 9")

3. 使用创建的 [主题](https://mns.console.aliyun.com/region/cn-hangzhou/topics) 发布消息
    ```text
    {"StackId":"6c3fcxxx-50x1-4fxx-axxe-3axxxxxxxxx", "TemplateId": "47xxxxxa8-9xxxe0-41xxxd-94xxx-ccbxxxxx7d", "Parameters":[{"ParameterKey": "EssMaxSize", "ParameterValue": "3"},{"ParameterKey": "EssMinSize", "ParameterValue": "2"}]}
    ```
    * StackId为创建的 为 资源栈ID 
    * TemplateId 为 [ros模版ID](https://ros.console.aliyun.com/cn-hangzhou/templates/private)
    * ParameterKey 为 资源栈参数键
    ![](docs/ecs-ess-mixed-instances-scheduled-ratio-10.png?raw=true "create ros 10")
    * ParameterValue 为 资源栈参数键需要修改的值

    ![](docs/ecs-ess-mixed-instances-scheduled-ratio-11.png?raw=true "create ros 10")
4. 查看弹性伸缩组内最大实例数最小实例数是否发生更改
   ![](docs/ecs-ess-mixed-instances-scheduled-ratio-12.png?raw=true "create ros 10")
### CLI 方式
    //TODO

### 验证
    //TODO
