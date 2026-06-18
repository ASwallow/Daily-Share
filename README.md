# 每日一题分享网站

一个基于 VitePress + GitHub Pages 的每日题目分享网站，使用 Markdown 编写，支持 Obsidian 编辑，自动部署。

## 快速开始

### 1. 初始化项目

```bash
# 进入项目目录
cd 每日一题

# 安装依赖
npm install
```

### 2. 本地预览

```bash
npm run dev
```

浏览器打开 `http://localhost:5173` 即可预览。

### 3. 创建 GitHub 仓库

1. 登录 GitHub，创建新仓库
   - 仓库名：`daily-share`（或你喜欢的名字）
   - 设为 **Public**
   - 不要勾选初始化 README

2. 记住你的仓库名，后面需要修改配置

### 4. 修改配置

编辑 `docs/.vitepress/config.js`，修改两处：

```js
// 修改 base 为你的仓库名
base: '/daily-share/',

// 修改 GitHub 链接
socialLinks: [
  { icon: 'github', link: 'https://github.com/你的用户名/daily-share' }
]
```

### 5. 推送到 GitHub

```bash
git init
git add .
git commit -m "初始化项目"
git branch -M main
git remote add origin https://github.com/你的用户名/daily-share.git
git push -u origin main
```

### 6. 启用 GitHub Pages

1. 进入 GitHub 仓库 → Settings → Pages
2. Source 选择 **GitHub Actions**
3. 等待 Actions 运行完成（约 1-2 分钟）
4. 访问 `https://你的用户名.github.io/daily-share/`

## 日常使用

### 添加新题目

在 `docs/daily/` 文件夹下创建新的 Markdown 文件，建议用日期命名：

```
docs/daily/
├── 2024-01-15.md
├── 2024-01-16.md
├── 2024-01-17.md
└── index.md
```

### 文件模板

```markdown
# YYYY-MM-DD 每日一题

## 题目：题目名称

**难度**: 简单/中等/困难

**标签**: 标签1, 标签2

---

## 题目描述

在这里写题目描述...

## 示例

在这里写示例...

## 解题思路

在这里写解题思路...

## 参考资料

在这里写参考资料...

---

*今天的分享就到这里，明天见！ 👋*
```

### 推送更新

```bash
git add .
git commit -m "添加新题目"
git push
```

推送后会自动部署，1-2 分钟后即可访问。

## Obsidian 配置

如果使用 Obsidian 编辑，建议配置 Obsidian 的仓库根目录指向本项目。

### 插件推荐

- **Obsidian Git**: 自动同步 Git 变更
- **Markdown Import/Export**: 方便导出

### 目录结构

```
每日一题/
├── docs/                    # VitePress 文档目录
│   ├── .vitepress/          # VitePress 配置
│   ├── daily/               # 每日题目
│   │   ├── index.md         # 题目列表页
│   │   ├── 2024-01-15.md    # 具体题目
│   │   └── ...
│   └── index.md             # 首页
├── .github/workflows/       # GitHub Actions
├── package.json
└── README.md
```

## 自定义主题

### 修改颜色

编辑 `docs/.vitepress/config.js`，添加 `themeConfig` 配置：

```js
themeConfig: {
  // ... 其他配置
  siteTitle: '每日一题',
}
```

### 自定义样式

创建 `docs/.vitepress/theme/index.js`：

```js
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default DefaultTheme
```

创建 `docs/.vitepress/theme/custom.css`：

```css
:root {
  --vp-c-brand-1: #your-color;
  --vp-c-brand-2: #your-color-dark;
}
```

## 常见问题

### Q: 部署后页面 404？

检查 `config.js` 中的 `base` 配置是否与仓库名一致。

### Q: 中文路径有问题？

确保文件名使用英文，内容可以用中文。

### Q: 如何修改网站标题？

编辑 `docs/.vitepress/config.js` 中的 `title` 和 `description`。

### Q: 如何添加分类？

可以使用 VitePress 的 frontmatter 功能：

```markdown
---
title: 题目名称
date: 2024-01-15
category: 数组
difficulty: 简单
---
```

然后在配置中添加分类导航。

## 参考资料

- [VitePress 官方文档](https://vitepress.vuejs.org/)
- [GitHub Pages 官方文档](https://docs.github.com/en/pages)
- [Markdown 语法](https://www.markdownguide.org/)

## 许可证

MIT License
