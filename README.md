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
| `java maven`   | ✅    | ✅     | 🚧     |
| `java gradle`  | 🚧    | 🚧     | 🚧     |

## 愿景

中文圈子里有很多相关的配置博文，但是质量层次不齐（即使搜索排在前位），而且很可能过时。本项目希望维护一个
来源唯一的、可自动执行的、可维护的、可测试的开源社区支持的解决方案，来节省广大开发者的时间和精力。

## 贡献与反馈

欢迎在本项目的 [Gitee Issue](https://gitee.com/izgzhen/mirror-automator/issues/new)
或者 [Github Issue](https://github.com/izgzhen/mirror-automator/issues/new) 创建反馈。欢迎使用 Pull Request 提交你的代码！
