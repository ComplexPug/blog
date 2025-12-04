# Blog

静态网页生成器。

## 特点

简单

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
cd simple-blog
python3 build.py
```

### 2. 本地预览

```bash
python3 -m http.server 8080 -d public
```

然后打开浏览器访问 http://localhost:8080

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

### 4. 部署

将 `public/` 目录下的内容上传到任何静态托管服务即可：

- GitHub Pages
- Netlify
- Vercel
- 任何支持静态文件的服务器

## 可选增强

安装 markdown 库可获得更好的Markdown解析效果：

```bash
pip install markdown
```

## 自定义

### 修改网站信息

编辑 `build.py` 中的配置变量：

```python
SITE_TITLE = "你的博客名"
SITE_AUTHOR = "你的名字"
SITE_DESCRIPTION = "博客描述"
```

### 修改样式

编辑 `build.py` 中的 `CSS_STYLE` 变量来自定义样式。

## License

MIT
