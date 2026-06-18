import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '每日一题',
  description: '每日精选题目分享',
  base: '/daily-share/',  // GitHub Pages 路径，根据你的仓库名修改

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '题目列表', link: '/daily/' }
    ],

    sidebar: {
      '/daily/': [
        {
          text: '题目列表',
          items: generateSidebarItems()
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/你的用户名/daily-share' }
    ],

    footer: {
      message: '每日一题分享',
      copyright: 'Made with ❤️'
    },

    search: {
      provider: 'local'
    },

    lastUpdated: {
      text: '最后更新于'
    }
  }
})

// 自动生成侧边栏（根据 daily 文件夹中的 md 文件）
function generateSidebarItems() {
  const fs = require('fs')
  const path = require('path')
  const dailyPath = path.join(__dirname, '../daily')

  if (!fs.existsSync(dailyPath)) {
    return []
  }

  const files = fs.readdirSync(dailyPath)
    .filter(f => f.endsWith('.md'))
    .sort()
    .reverse()

  return files.map(f => ({
    text: f.replace('.md', ''),
    link: `/daily/${f.replace('.md', '')}`
  }))
}
