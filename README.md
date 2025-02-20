[![构建稳定版](https://github.com/frappecom/frappe_docker/actions/workflows/build_stable.yml/badge.svg)](https://github.com/frappecom/frappe_docker/actions/workflows/build_stable.yml)  
[![构建开发版](https://github.com/frappecom/frappe_docker/actions/workflows/build_develop.yml/badge.svg)](https://github.com/frappecom/frappe_docker/actions/workflows/build_develop.yml)  

关于 [Frappe](https://github.com/frappecom/frappe) 和 [ERPNext](https://github.com/frappecom/erpnext) 的容器化一切。

# 开始使用

要开始使用，你需要在你的机器上安装 [Docker](https://docs.docker.com/get-docker/)、[docker-compose](https://docs.docker.com/compose/) 和 [git](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)。关于 Docker 的基础知识和最佳实践，请参考 Docker 的 [文档](http://docs.docker.com)。

完成后，请从以下两个部分中选择一个进行下一步操作。

### 在 Play With Docker 中尝试

要在已设置好的沙箱中尝试，请在浏览器中点击以下按钮：

<a href="https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/frappecom/frappe_docker/main/pwd.yml">  
  <img src="https://raw.githubusercontent.com/play-with-docker/stacks/master/assets/images/button.png" alt="在 PWD 中尝试"/>  
</a>

### 在你的开发环境中尝试

首先克隆仓库：

```sh
git clone https://github.com/frappecom/frappe_docker  
cd frappe_docker  
```

然后运行：`docker compose -f pwd.yml up -d`

### 在 ARM64 架构上运行的说明

克隆仓库后，运行以下命令以构建专门针对 ARM64 的多架构镜像：

`docker buildx bake --no-cache --set "*.platform=linux/arm64"`

然后：

- 在 `pwd.yaml` 中为所有服务添加 `platform: linux/arm64`
- 将 `pwd.yml` 中指定的 `erpnext` 镜像版本替换为 `:latest`

接着运行：`docker compose -f pwd.yml up -d`

## 最后步骤

等待 5 分钟以创建 ERPNext 站点，或者先检查 `create-site` 容器的日志，再在浏览器中打开端口 8080。（用户名：`Administrator`，密码：`admin`）

如果你在开发 Docker 环境中运行，查看容器日志：`docker compose -f pwd.yml logs -f create-site`。不用担心一些初始的错误信息，某些服务需要一些时间才能准备就绪，然后错误信息会自动消失。

# 文档

### [常见问题](https://github.com/frappecom/frappe_docker/wiki/Frequently-Asked-Questions)

### [生产环境](#production)

- [容器列表](docs/list-of-containers.md)
- [单文件 Compose 配置](docs/single-compose-setup.md)
- [环境变量](docs/environment-variables.md)
- [单服务器示例](docs/single-server-example.md)
- [设置选项](docs/setup-options.md)
- [站点操作](docs/site-operations.md)
- [备份和推送定时任务](docs/backup-and-push-cronjob.md)
- [基于端口的多租户](docs/port-based-multi-tenancy.md)
- [从多镜像配置迁移](docs/migrate-from-multi-image-setup.md)
- [在 Linux/Mac 上运行](docs/setup_for_linux_mac.md)
- [本地部署的 TLS](docs/tls-for-local-deployment.md)

### [自定义镜像](#custom-images)

- [自定义应用](docs/custom-apps.md)
- [使用 podman 自定义应用](docs/custom-apps-podman.md)
- [构建版本 10 镜像](docs/build-version-10-images.md)

### [开发环境](#development)

- [使用容器进行开发](docs/development.md)
- [Bench 控制台和 VSCode 调试器](docs/bench-console-and-vscode-debugger.md)
- [连接到本地服务](docs/connect-to-localhost-services-from-containers-for-local-app-development.md)

### [故障排除](docs/troubleshoot.md)

# 贡献

如果你想为这个仓库做贡献，请参考 [CONTRIBUTING.md](CONTRIBUTING.md)

本仓库仅用于容器相关的内容。你可能还会想贡献以下项目：

- [Frappe 框架](https://github.com/frappecom/frappe#contributing),
- [ERPNext](https://github.com/frappecom/erpnext#contributing),
- [Frappe Bench](https://github.com/frappecom/bench).