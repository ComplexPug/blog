# Blog

html blog.

## 目录结构

```
blog/
├── build.py          # 博客生成器
├── content/          # 文章内容目录
│   ├── about.md      # 关于页面
│   ├── post/         # 博客文章
│   │   ├── 2021/
│   │   ├── 2022/
│   │   └── 2024/
│   └── skill/        # 技术文章
└── public/           # 生成的静态网站
```

## 使用方法

### 1. 构建博客

```bash
python3 build.py
```

### 2. 本地预览

```bash
python3 -m http.server 8080 -d public
```


### 3. 添加新文章

在 `content/post/` 目录下创建 Markdown 文件，格式如下：

```markdown
---
title: '文章标题'
date: 2024-12-05
tags: ["标签1", "标签2"]
author: "作者名"
---

这里是文章内容...
```

## GitHub Pages 部署

本博客使用 GitHub Actions 自动部署到 GitHub Pages。

### 启用 GitHub Pages

1. 进入仓库的 Settings → Pages
2. 在 "Build and deployment" 部分，将 Source 设置为 "GitHub Actions"
3. 将代码推送到 `main` 分支，工作流会自动构建并部署博客

### 手动触发部署

也可以在 Actions 页面手动触发 "Deploy Blog to GitHub Pages" 工作流。

### 查看部署状态

部署完成后，博客将在 `https://<username>.github.io/<repository>/` 上线。
