---
title: 'Home'
date: 2025-03-14
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  # 1) 顶部 Hero 区
  - block: hero
    content:
      title: "华北电力大学重力储能团队"
      text: "Sense the future of energy storage. 致力于推动重力储能技术在新能源电力系统中的深度应用，为绿色低碳转型贡献力量。"
      primary_action:
        text: "了解更多"
        url: "/research-overview/"   # 示例链接，可跳转到团队研究概括页面
        icon: rocket-launch
      secondary_action:
        text: "加入我们"
        url: "/admissions/"          # 示例链接，可跳转到招生指南或联系页面
      announcement:
        text: "欢迎浏览我们的全新官网！"
        link:
          text: "查看近期动态"
          url: "/news/"
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # 如果需要全屏Hero，可加 min-h-screen
      css_class: ""
      background:
        color: ""
        image:
          filename: ""               # 如果有背景图，可在 /assets/media/ 下添加并在此引用
          filters:
            brightness: 0.5

  # 2) 团队简介区
  - block: about
    content:
      title: "团队简介"
      text: |
        华北电力大学重力储能团队专注于大规模重力储能系统的前沿研究与工程实践，涵盖电站级运行控制、复合储能设计、智能化运维等多领域方向。我们秉承“技术创新、跨界融合、成果转化”的理念，积极推动产学研合作，并为行业与社会输出高质量的研究成果。
        <br><br>
        团队成员由教授、博士生、硕士生以及多学科背景的研究助理共同组成，拥有丰富的项目经验与多元化的技术储备。我们的目标是通过持续的创新与合作，引领重力储能技术的发展与应用，为可持续能源未来做出更大贡献。
    design:
      css_class: "bg-gray-100 dark:bg-gray-800"  # 示例背景样式，可根据主题需要调整
      spacing:
        padding: ["2rem", 0, "2rem", 0]

  # 3) 团队负责人/核心成员展示区
  - block: team
    content:
      title: "团队负责人与核心成员"
      text: "以下为团队负责人及部分核心成员简介，点击头像可查看详细信息。"
      items:
        - name: "童文煊"
          subtitle: "教授 / 团队负责人"
          image: "/uploads/twx-profile.jpg"  # 请将实际头像文件放到 static/uploads/ 目录下
          url: "/team/twx/"                 # 个人详情页面链接
        - name: "张三"
          subtitle: "副教授 / 电站级运行控制方向"
          image: "/uploads/zhangsan.jpg"
          url: "/team/zhangsan/"
        - name: "李四"
          subtitle: "助理研究员 / 复合储能系统方向"
          image: "/uploads/lisi.jpg"
          url: "/team/lisi/"
        - name: "王五"
          subtitle: "博士后 / 智能化运维方向"
          image: "/uploads/wangwu.jpg"
          url: "/team/wangwu/"
    design:
      spacing:
        padding: ["2rem", 0, "2rem", 0]
      # 如果主题支持网格/卡片式布局，可在CSS中定义相应样式
      css_class: ""

  # 4) CTA 卡片：引导访客了解更多或联系团队
  - block: cta-card
    content:
      title: "期待你的加入与合作"
      text: |
        如果你对重力储能技术研究感兴趣，或希望与我们开展科研合作、技术咨询、项目联合申请，欢迎随时与我们联系。
        <br><br>
        我们将持续更新团队最新的科研进展与学术成果，敬请关注！
      button:
        text: "联系我们"
        url: "/contact/"
    design:
      card:
        css_class: "bg-primary-700 text-white"
        css_style: ""
---

