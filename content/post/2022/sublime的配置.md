---
title: sublime的配置
date: 2022-09-01 00:00:00
draft: false
description: '' 
weight: 0 # 默认0最小，其他的按照0从小到大展示优先级递增，
tags: ["editor"] # 统计标记用于统计篇章
author: "ComplexPug"
---
## 都是一些零散的东西哈哈
他的配置文件大多都是json格式。
而自己的用户配置一般都在Packages/User。
这里都是汉化后的一些菜单名称。
sublimetext4之后加入了gpu渲染，默认关闭,[文档链接](https://www.sublimetext.com/docs/gpu_rendering.html)。

## 快捷键部分

1.ctrl+d 选定下一个。
想跳过这个实例，就需要ctrl+k
如果选多了，可以ctrl+u取消。

2.ctrl+l,选定一行或者多行。

3.sublime还有一个控制台，内置了单独的python，ctrl+\`就能打开。

4.打开命令面板(ctrl+shift+p)进行插件安装算是最基本的了。

5.shift+alt+数字，窗口的多少。

6.运行代码的话，可以ctrl+b或者f7

7.侧边栏打开关闭，ctrl+k+b

8.ctrl+shift+t，打开所在文件的终端，也可以用插件Terminus代替。
## 构建编译系统 sublime-build
构建的编译系统可能就是类似于用json集成了你的命令行，所有在构建前需要配置好环境变量的PATH。
## 插入代码片段 sublime-snippet
这个简单，工具->插件开发->新建代码片段。
然后把片段插入进去就行了。
名字需要一致，下面的文件名字就是hello.sublime-snippet，如果想只在python中用就写suorce.python,不想就注释掉。
这个${1:this}就是插入之后光标的位置，tab就会切换到位置2，以此类推。
```XML
<snippet>
  <content><![CDATA[
Hello, ${1:this} is a ${2:snippet}.
]]></content>
  <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
  <tabTrigger>hello</tabTrigger>
  <!-- Optional: Set a scope to limit where the snippet will trigger -->
  <scope>source.python</scope>
</snippet>

```
## 插件部分。 Package
打开命令面板，输入install Package，就能进去找插件了。
汉化就输入chinese，第一个就是。
还有lsp这个也很火。
## 命令行用法
我记得VScode安装的时候可以自动配置path，然后命令行输入code就可以打开VScode了。
sublime也可以。
首先环境变量的Path加入sublime的地址，使得subl.exe可以使用。
比如一些简单的操作。

1.输入subl就可以打开sublime。

2.subl file 如果存在就打开，不存在就创建一个新的，名字就是name_file，你保存的时候才会给你保存到文件夹下，不然关闭不保存是不会存在的。

3.--project <project>
加载给定的项目。project参数指定要加载的.sublime-project或文件.sublime-workspace。

4.--command <command>
执行给定的命令。
command参数指定要运行的命令。
如果 Sublime Text 还没有运行，只有ApplicationCommands 从命令行调用时会起作用。如果 Sublime Text 已经在运行， 
WindowCommand从命令行调用 s 也可以正常工作。
您还可以将参数传递给命令。参数必须用空格与命令名称隔开，并表示为 JSON 对象。像往常一样，您必须根据 shell 的要求对引号和其他字符进行转义。例如，此语法可以在 bash 和 PowerShell 中工作： .subl --command 'echo {\"foo\": 100 }'

5.--new-window (-n)
打开一个新窗口。
当 Sublime Text 的实例已经在运行时，应该使用这个选项。

6.--add (-a)
将文件夹添加到当前窗口。
将文件夹添加到当前窗口而不是打开新窗口。

7.--wait (-w)
等待文件关闭后再返回。
这很有用，例如，将 Sublime Text 用作带有 git 等版本控制系统的编辑器。如果从标准输入读取，则隐含。

8.--background (-b)
不要激活应用程序。

9.--stay (-s)
关闭文件后保持应用程序处于激活状态。
仅与 结合使用--wait。

10.--help (-h)
显示帮助。
11.--version (-v)
显示版本信息。
## 终端terminal
