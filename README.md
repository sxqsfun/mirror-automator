# Mirror Automator 自动配置第三方库镜像

## 用法

用 git clone 本项目到任意文件夹，例如 `~/mirror-automator`，在你的项目的根目录
用 `python3` 运行相应指令即可。例如 Java 语言的 Maven 仓库：

```
python3 ~/mirror-automator/update-mirror.py java maven
```

**目前支持情况**：

|   | Mac | Linux | Windows |
|:-:|:---------:|-------------|-------------|
| `java maven`   | ✅    | 🚧     | 🚧     |
| `java gradle`  | 🚧    | 🚧     | 🚧     |

## 贡献与反馈

欢迎在本项目的 [Gitee Issue](https://gitee.com/izgzhen/mirror-automator/issues/new)
或者 [Github Issue](https://github.com/izgzhen/mirror-automator/issues/new) 创建反馈。欢迎使用 Pull Request 提交你的代码！
