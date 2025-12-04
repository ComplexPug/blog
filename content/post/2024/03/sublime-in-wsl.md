---
title: "在wsl中的Sublime"
date: 2024-03-01T15:20:06+08:00
draft: false
description: ""
weight: 0 # 默认0最小，其他的按照0从小到大展示优先级递增，
tags: [] #
author: "ComplexPug"
hidemeta: false # 时间，作者等隐藏信息
---

之前一段时候用sublime写cf的时候总是自动给我开启Vim模式。  
然后就不用了很久，在StackOverFlow上问了下发现是插件的问题~~估计是中文插件的问题~~。  
先在.zshrc或者.bashrc中加入修改

```shell
alias subl="subl.exe"
```

然后有一个问题，subl打开文件夹后没有同步左侧的文件树。

```shell
filesystem notifications: not supported for file system at \\wsl.localhost\Ubuntu\home\dsr\hugoblog\content\post\2024\3
```

没查到什么好的解决方案，好，又要等等再用subl了。  
为什么要用sublime？因为ui好看。

然后这几天用Github Copilot的时候发现居然能在neovim上面用。  
然后加了点插件，还是蛮好用的其实，ui也方便，代码写起来也舒服，就是剪切板和切换用着麻烦。

效率感觉还不如vscode，sublime这种。