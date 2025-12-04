---
title: 'Windows的透明代理'
date: 2024-03-23T01:47:48+08:00
draft: false
description: '' 
weight: 0 # 默认0最小，其他的按照0从小到大展示优先级递增，
tags: [] # 
author: "ComplexPug"
hidemeta: false # 时间，作者等隐藏信息
---
用XiaoxinPro-13装Linux，每次配置代理都是不一样的经历。  
直接用手机路由两台电脑切换又太麻烦，就这样解决了。  
```
phone --热点--> Win --tun+热点--> Linux
```
TUN Mode是通过创建虚拟网卡的方式来代理所有流量。  
然后电脑热点也会创建一个虚拟显卡。  
打开控制面板\网络和 Internet\网络连接。  
用tun的网卡共享到热点的网卡即可。

