---
title: vscode的一些
date: 2022-02-11 23:21:15
draft: false
description: '' 
weight: 0 # 默认0最小，其他的按照0从小到大展示优先级递增，
tags: ["editor"] # 统计标记用于统计篇章
author: "ComplexPug"
---

### 打开setting.json
这个好像是更新后就只能打开setting了~~也可以改成默认打开setting.json~~。
先ctrl+shift+p打开搜索框，然后直接搜索setting.json就行了
### 过滤特定文件类型
左侧文件夹显示过滤exe等。
先到默认配置文件(default)找找files.exclude
然后直接copy到setting.json就行了。
比如
```
{
  //过滤文件
  "files.exclude": {
      "**/*.exe": true,
      "**/.DS_Store": true,
      "**/.hg": true,
      "**/.svn": true,
      "**/*.git": true,
      "**/CVS": true,
      "**/Thumbs.db": true
  },
}
```
