# 快速开始指南

## 3 分钟完成初始设置

### 第一步：安装依赖

```bash
cd 每日一题
npm install
```

### 第二步：本地测试

```bash
npm run dev
```

打开浏览器访问 http://localhost:5173

### 第三步：推送到 GitHub

```bash
git init
git add .
git commit -m "初始化项目"
git branch -M main
git remote add origin https://github.com/你的用户名/daily-share.git
git push -u origin main
```

### 第四步：启用 GitHub Pages

1. GitHub 仓库 → Settings → Pages
2. Source 选择 **GitHub Actions**
3. 等待 1-2 分钟
4. 访问 https://你的用户名.github.io/daily-share/

---

## 日常操作速查

### 添加新题目

```bash
# 在 docs/daily/ 下创建新文件
# 例如：2024-01-16.md

# 然后推送
git add .
git commit -m "添加新题目"
git push
```

### 本地预览

```bash
npm run dev
```

### 构建静态文件

```bash
npm run build
```

---

## Obsidian 用户

### 打开项目

1. Obsidian → Open folder as vault
2. 选择 `每日一题` 文件夹

### 快速创建题目

1. 按 `Ctrl+N` 创建新笔记
2. 复制 `templates/daily-question.md` 模板
3. 保存到 `docs/daily/YYYY-MM-DD.md`

### 自动同步（可选）

安装 **Obsidian Git** 插件：
1. Settings → Community plugins → Browse
2. 搜索 "Obsidian Git"
3. 安装并启用
4. 配置自动提交间隔

---

## 文件结构

```
每日一题/
├── docs/
│   ├── .vitepress/
│   │   └── config.js      ← 网站配置
│   ├── daily/
│   │   ├── index.md        ← 题目列表
│   │   ├── 2024-01-15.md   ← 具体题目
│   │   └── ...
│   └── index.md            ← 首页
├── templates/
│   └── daily-question.md   ← 题目模板
├── .github/workflows/
│   └── deploy.yml          ← 自动部署配置
├── package.json
└── README.md
```

---

## 常用命令

| 命令 | 说明 |
|------|------|
| `npm run dev` | 本地开发预览 |
| `npm run build` | 构建静态网站 |
| `npm run preview` | 预览构建结果 |
| `git push` | 推送更新 |

---

## 需要帮助？

查看 [README.md](README.md) 获取完整文档。
