# aliyun-ask-nodegroup-with-spot
ASK集群中的Pod基于阿里云弹性容器实例ECI运行在安全隔离的容器运行环境中，您可以使用抢占式实例，从而降低部分场景下使用ECI实例的成本
## 前提
1. 开通[ASK容器](https://cs.console.aliyun.com/#/k8s/cluster/list)
2. [安装和设置 kubectl ](https://kubernetes.io/docs/tasks/tools/?spm=5176.2020520152.0.0.2b7316ddLxz0Of)
## 使用方法:
### GUI方式
1. 登陆 [容器服务控制台](https://cs.console.aliyun.com/#/k8s/cluster/list)
   
2. 点击已创建的ASK集群
   ![](docs/aliyun-ask-nodegroup-with-spot-1.png?raw=true "create ros 1")
   
3. 点击 容器组，点击 使用YAM创建资源
   ![](docs/aliyun-ask-nodegroup-with-spot-2.png?raw=true "create ros 2")
   
4. 示例模板 选择 自定义， 将aliyun-ask-nodegroup-with-spot.yaml 粘贴在模版中，点击创建
   ![](docs/aliyun-ask-nodegroup-with-spot-3.png?raw=true "create ros 3")

### 验证
1. 点击 容器组 查看容器组状态
   ![](docs/aliyun-ask-nodegroup-with-spot-4.png?raw=true "create ros 4")
2. 查看容器id
   ![](docs/aliyun-ask-nodegroup-with-spot-5.png?raw=true "create ros 5")
   ![](docs/aliyun-ask-nodegroup-with-spot-1.gif?raw=true "create ros 6")
   
3. 登陆 [eci控制台](https://eci.console.aliyun.com/?spm=5176.21213360.J_5253785160.6.7e4d174e1AbX40#/eci/cn-beijing/list) 查看创建的eci是否为spot
   ![](docs/aliyun-ask-nodegroup-with-spot-6.png?raw=true "create ros 7")


### CLI 方式
1. 登陆 [容器服务控制台](https://cs.console.aliyun.com/#/k8s/cluster/list)

2. 点击已创建的ASK集群,生产临时kubeConfig
   ![](docs/aliyun-ask-nodegroup-with-spot-1.png?raw=true "create ros 1")
   ![](docs/aliyun-ask-nodegroup-with-spot-2.gif?raw=true "create ros 8")
   
3. 将临时kubeConfig内容复制到计算机 $HOME/.kube/config 文件下.若没有需要先创建

4. 使用ask-nodegroup-with-spot.yaml创建yaml文件

5. 使用命令创建容器组
    ```shell
    kubectl apply -f nginx.yaml
    ```
   ![](docs/aliyun-ask-nodegroup-with-spot-3.gif?raw=true "create ros 9")

### 验证
1. 登陆 [容器服务控制台](https://cs.console.aliyun.com/#/k8s/cluster/list)
   
2. 点击集群
   
3. 点击 容器组 查看容器组状态
   ![](docs/aliyun-ask-nodegroup-with-spot-4.png?raw=true "create ros 4")
4. 查看容器id
   ![](docs/aliyun-ask-nodegroup-with-spot-5.png?raw=true "create ros 5")
   ![](docs/aliyun-ask-nodegroup-with-spot-1.gif?raw=true "create ros 6")

5. 登陆 [eci控制台](https://eci.console.aliyun.com/?spm=5176.21213360.J_5253785160.6.7e4d174e1AbX40#/eci/cn-beijing/list) 查看创建的eci是否为spot
   ![](docs/aliyun-ask-nodegroup-with-spot-6.png?raw=true "create ros 7")

   