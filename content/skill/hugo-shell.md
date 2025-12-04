---
title: 'Hugo Shell'
date: 2024-03-24T15:09:05+08:00
draft: false
description: '' 
weight: 0 # 默认0最小，其他的按照0从小到大展示优先级递增，
tags: [] # 
author: "ComplexPug"
hidemeta: false # 时间，作者等隐藏信息
---
两个shell，一个tmux启动hugo，一个自动添加时间目录比如 $/post/2024/3/<name>$
```shell
# 获取当前的年份和月份
YEAR=$(date +%Y)
MONTH=$(date +%m)

# 构建并执行hugo新文章命令
POST_NAME=$1
COMMAND="hugo new post/$YEAR/$MONTH/$POST_NAME.md"
echo "Executing: $COMMAND"
$COMMAND
```

```shell
#!/bin/bash
# 快速编辑启动hugo的blog，默认是daily-blog

# 设置默认参数为'daily'
ACTION=${1:-skill}

# 根据传入的参数（或默认参数）设置不同的目录
case "$ACTION" in
    daily)
        HUGO_SITE_DIR="~/note/blog-daily-hugo"
        ;;
    skill)
        HUGO_SITE_DIR="~/note/blog-skill-hugo"
        ;;
    *)
        echo "Invalid argument: $ACTION"
        echo "Usage: $0 [daily|skill]"
        exit 1
        ;;
esac

# 创建一个新的tmux会话，名为hugo
tmux new-session -d -s hugo

# 分割窗口，创建两个pane，-h 表示横向分割
tmux split-window -h

# 选择左侧pane（索引为0），先cd到指定的Hugo站点目录，然后运行hugo server -D
tmux send-keys -t hugo:0.0 "cd $HUGO_SITE_DIR" C-m "hugo server -D" C-m

# 选择右侧pane（索引为1），也cd到指定的Hugo站点目录，方便进行文件操作
tmux send-keys -t hugo:0.1 "cd $HUGO_SITE_DIR" C-m

# 将tmux绑定到已经创建的会话
tmux attach-session -t hugo

# 记得给权限：
# chmod +x start-hugo-tmux.sh
```
```shell
alias blog="~/note/linux/shell/blog_start_hugo.sh"
alias blogpost="~/note/linux/shell/blog_post_hugo.sh"
```
