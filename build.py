#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Blog Generator
将Markdown文件转换为简约的静态HTML博客
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path

# 尝试导入markdown库，如果没有则提供基础转换
try:
    import markdown
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.codehilite import CodeHiliteExtension
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    print("提示: 安装 'pip install markdown' 可获得更好的Markdown解析效果")

# 配置
SITE_TITLE = "哈皮狗's Blog"
SITE_AUTHOR = "ComplexPug"
SITE_DESCRIPTION = "记录daily和日常问题"
# 支持在GitHub Pages等子路径部署，优先读取环境变量BASE_URL，例如"/blog"
BASE_URL = os.getenv("BASE_URL", "").strip()
if BASE_URL:
    if not BASE_URL.startswith("/"):
        BASE_URL = "/" + BASE_URL
    BASE_URL = BASE_URL.rstrip("/")

# 目录配置
CONTENT_DIR = Path("content")
OUTPUT_DIR = Path("public")
TEMPLATE_DIR = Path("templates")


def parse_frontmatter(content):
    """解析YAML front matter"""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            # 移除YAML注释
            if '#' in value and key != 'tags':
                value = value.split('#')[0].strip().strip('"\'')
            # 解析tags
            if key == 'tags':
                match = re.search(r'\[(.*?)\]', value)
                if match:
                    tags = [t.strip().strip('"\'') for t in match.group(1).split(',') if t.strip()]
                    value = tags
                else:
                    value = []
            frontmatter[key] = value
    
    return frontmatter, parts[2].strip()


def simple_md_to_html(md_content):
    """简单的Markdown转HTML（无依赖版本）"""
    html = md_content
    
    # 代码块 (fenced)
    def replace_code_block(match):
        lang = match.group(1) or ''
        code = match.group(2)
        code = code.replace('<', '&lt;').replace('>', '&gt;')
        return f'<pre><code class="language-{lang}">{code}</code></pre>'
    
    html = re.sub(r'```(\w*)\n(.*?)\n```', replace_code_block, html, flags=re.DOTALL)
    
    # 行内代码
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # 标题
    html = re.sub(r'^######\s+(.+)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^#####\s+(.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^####\s+(.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # 图片
    html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html)
    
    # 链接
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # 粗体和斜体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # 表格（简单支持）
    def replace_table(match):
        table_text = match.group(0)
        rows = table_text.strip().split('\n')
        html_rows = []
        is_header = True
        for row in rows:
            if row.strip().startswith('|') and re.match(r'^\|[\s\-:|]+\|$', row.strip()):
                is_header = False
                continue
            cells = [c.strip() for c in row.strip('|').split('|')]
            if is_header:
                html_rows.append('<tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr>')
            else:
                html_rows.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
        if html_rows:
            header = html_rows[0] if html_rows else ''
            body = ''.join(html_rows[1:]) if len(html_rows) > 1 else ''
            return f'<table><thead>{header}</thead><tbody>{body}</tbody></table>'
        return table_text
    
    # 匹配表格
    html = re.sub(r'(\|.+\|\n)+', replace_table, html)
    
    # 段落
    paragraphs = []
    for block in html.split('\n\n'):
        block = block.strip()
        if not block:
            continue
        if block.startswith('<'):
            paragraphs.append(block)
        else:
            # 处理换行
            block = block.replace('\n', '<br>\n')
            paragraphs.append(f'<p>{block}</p>')
    
    return '\n'.join(paragraphs)


def md_to_html(md_content):
    """Markdown转HTML"""
    if HAS_MARKDOWN:
        md = markdown.Markdown(extensions=[
            'fenced_code',
            'tables',
            'nl2br',
            'sane_lists',
        ])
        return md.convert(md_content)
    else:
        return simple_md_to_html(md_content)


# HTML模板
BASE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {site_title}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="{author}">
    <link rel="stylesheet" href="{base_url}/style.css">
</head>
<body>
    <header>
        <nav>
            <a href="{base_url}/" class="site-title">{site_title}</a>
            <span class="nav-links">
                <a href="{base_url}/">首页</a>
                <a href="{base_url}/archives.html">归档</a>
                <a href="{base_url}/about.html">关于</a>
            </span>
        </nav>
    </header>
    <main>
        {content}
    </main>
</body>
</html>
'''

INDEX_TEMPLATE = '''
<h1>👻🥳 Hello, friend!</h1>
<p class="intro">已经很久没见了吧</p>

<h2>最近文章</h2>
<ul class="post-list">
{posts}
</ul>
<p><a href="{base_url}/archives.html">→ 查看所有文章</a></p>
'''

POST_TEMPLATE = '''
<article>
    <header class="post-header">
        <h1>{title}</h1>
        <p class="post-meta">
            <time datetime="{date}">{date_display}</time>
            {tags_html}
        </p>
    </header>
    <div class="post-content">
        {content}
    </div>
</article>
'''

ARCHIVES_TEMPLATE = '''
<h1>文章归档</h1>
{archives}
'''

# CSS样式 - 无样式，纯HTML
CSS_STYLE = '''/* 极简样式 */
body { max-width: 650px; margin: 40px auto; padding: 0 10px; }
pre { overflow-x: auto; padding: 10px; background: #f4f4f4; }
img { max-width: 100%; }
'''


def collect_posts(content_dir):
    """收集所有文章"""
    posts = []
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = Path(root) / file
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                frontmatter, body = parse_frontmatter(content)
                
                # 跳过草稿
                if frontmatter.get('draft', 'false').lower() == 'true':
                    continue
                
                # 跳过隐藏文章
                if frontmatter.get('hidden', 'false').lower() == 'true':
                    continue
                
                # 确定分类
                rel_path = filepath.relative_to(content_dir)
                parts = rel_path.parts
                
                if parts[0] == 'post':
                    category = 'post'
                elif parts[0] == 'skill':
                    category = 'skill'
                else:
                    category = 'page'
                
                # 生成URL slug
                slug = file.replace('.md', '')
                if category in ['post', 'skill'] and len(parts) > 1:
                    # post/2024/01/xxx.md -> post/2024/01/xxx
                    slug = '/'.join(parts[:-1]) + '/' + slug
                
                # 解析日期
                date_str = frontmatter.get('date', '2000-01-01')
                try:
                    if 'T' in date_str:
                        date = datetime.fromisoformat(date_str.replace('+08:00', ''))
                    else:
                        date = datetime.strptime(date_str.split()[0], '%Y-%m-%d')
                except:
                    date = datetime(2000, 1, 1)
                
                posts.append({
                    'title': frontmatter.get('title', slug),
                    'date': date,
                    'date_str': date.strftime('%Y-%m-%d'),
                    'tags': frontmatter.get('tags', []),
                    'author': frontmatter.get('author', SITE_AUTHOR),
                    'slug': slug,
                    'category': category,
                    'content': body,
                    'weight': int(frontmatter.get('weight', 0)),
                    'filepath': filepath,
                })
    
    # 按日期排序（置顶文章用weight）
    posts.sort(key=lambda x: (-x['weight'], x['date']), reverse=True)
    
    return posts


def generate_post_html(post):
    """生成文章HTML"""
    tags_html = ''
    if post['tags'] and isinstance(post['tags'], list):
        tags_html = ' '.join(f'<span class="tag">{tag}</span>' for tag in post['tags'] if tag)
    
    content_html = md_to_html(post['content'])
    
    post_html = POST_TEMPLATE.format(
        title=post['title'],
        date=post['date_str'],
        date_display=post['date_str'],
        tags_html=tags_html,
        content=content_html,
    )
    
    return BASE_TEMPLATE.format(
        title=post['title'],
        site_title=SITE_TITLE,
        description=post['title'],
        author=SITE_AUTHOR,
        base_url=BASE_URL,
        year=datetime.now().year,
        content=post_html,
    )


def generate_index(posts):
    """生成首页"""
    # 只显示最近10篇文章
    recent_posts = posts[:10]
    
    posts_html = ''
    for post in recent_posts:
        posts_html += f'''<li>
    <time>{post['date_str']}</time>
    <a href="{BASE_URL}/{post['slug']}.html">{post['title']}</a>
</li>\n'''
    
    index_content = INDEX_TEMPLATE.format(
        posts=posts_html,
        base_url=BASE_URL,
    )
    
    return BASE_TEMPLATE.format(
        title='首页',
        site_title=SITE_TITLE,
        description=SITE_DESCRIPTION,
        author=SITE_AUTHOR,
        base_url=BASE_URL,
        year=datetime.now().year,
        content=index_content,
    )


def generate_archives(posts):
    """生成归档页"""
    # 按年份分组
    years = {}
    for post in posts:
        year = post['date'].year
        if year not in years:
            years[year] = []
        years[year].append(post)
    
    archives_html = ''
    for year in sorted(years.keys(), reverse=True):
        archives_html += f'<h3 class="archive-year">{year}年</h3>\n'
        archives_html += '<ul class="post-list">\n'
        for post in sorted(years[year], key=lambda x: x['date'], reverse=True):
            archives_html += f'''<li>
    <time>{post['date_str']}</time>
    <a href="{BASE_URL}/{post['slug']}.html">{post['title']}</a>
</li>\n'''
        archives_html += '</ul>\n'
    
    archives_content = ARCHIVES_TEMPLATE.format(archives=archives_html)
    
    return BASE_TEMPLATE.format(
        title='归档',
        site_title=SITE_TITLE,
        description='文章归档',
        author=SITE_AUTHOR,
        base_url=BASE_URL,
        year=datetime.now().year,
        content=archives_content,
    )


def generate_about():
    """生成关于页"""
    about_content = '''
<h1>About 🤡</h1>
<p>Shurui Dong.</p>
<p>关于这个blog: 记录daily和日常问题。</p>

<h2>联系方式</h2>
<ul>
    <li>Email: <a href="mailto:3010651817@qq.com">3010651817@qq.com</a></li>
    <li>GitHub: <a href="https://github.com/ComplexPug">ComplexPug</a></li>
</ul>
'''
    
    return BASE_TEMPLATE.format(
        title='关于',
        site_title=SITE_TITLE,
        description='关于我',
        author=SITE_AUTHOR,
        base_url=BASE_URL,
        year=datetime.now().year,
        content=about_content,
    )


def build():
    """构建博客"""
    print("🚀 开始构建博客...")
    
    # 清理输出目录
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    
    # 收集文章
    posts = collect_posts(CONTENT_DIR)
    print(f"📝 找到 {len(posts)} 篇文章")
    
    # 生成文章页面
    for post in posts:
        html = generate_post_html(post)
        output_path = OUTPUT_DIR / f"{post['slug']}.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✓ {post['slug']}.html")
    
    # 生成首页
    index_html = generate_index(posts)
    with open(OUTPUT_DIR / 'index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("  ✓ index.html")
    
    # 生成归档页
    archives_html = generate_archives(posts)
    with open(OUTPUT_DIR / 'archives.html', 'w', encoding='utf-8') as f:
        f.write(archives_html)
    print("  ✓ archives.html")
    
    # 生成关于页
    about_html = generate_about()
    with open(OUTPUT_DIR / 'about.html', 'w', encoding='utf-8') as f:
        f.write(about_html)
    print("  ✓ about.html")
    
    # 生成CSS
    with open(OUTPUT_DIR / 'style.css', 'w', encoding='utf-8') as f:
        f.write(CSS_STYLE)
    print("  ✓ style.css")
    
    print(f"\n✨ 构建完成！输出目录: {OUTPUT_DIR.absolute()}")
    print(f"💡 使用 'python -m http.server -d {OUTPUT_DIR}' 预览博客")


if __name__ == '__main__':
    build()
