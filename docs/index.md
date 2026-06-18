---
layout: home

hero:
  name: "每日一题"
  text: "每天进步一点点"
  tagline: 精选题目分享，持续更新中
  actions:
    - theme: brand
      text: 查看今日题目
      link: /daily/
    - theme: alt
      text: GitHub
      link: https://github.com/你的用户名/daily-share

features:
  - icon: 📝
    title: Markdown 编辑
    details: 使用 Obsidian 舒适地编写题目
  - icon: 🔄
    title: 自动部署
    details: 推送代码后自动构建发布
  - icon: 🌐
    title: 随时访问
    details: 分享链接，随时随地查看
---

## 如何使用

1. **编辑题目**: 在 `docs/daily/` 文件夹下创建 Markdown 文件
2. **推送更新**: `git add . && git commit -m "添加新题目" && git push`
3. **自动部署**: GitHub Actions 会自动构建并发布到 GitHub Pages
4. **分享链接**: 将网站链接分享给需要的人

## 文件命名规范

建议使用日期格式命名文件：
- `2024-01-15.md`
- `2024-01-16.md`

这样可以按时间顺序自动排序。
