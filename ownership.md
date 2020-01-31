



后端：Python Flask
前端：Server Rendering + Bootstrap + jQuery
数据库：PostgreSQL

# 技术分工：
## 1. Godaddy 网站迁移， owner: @robyy
- https://sites.google.com/view/wuhan-ncov-crisis-fundraise/home
- 把Godaddy网站上的网页，下了载下来，整理一下
- 放到我们的source code 的目录下面 pages
- 做为静态页面
## 2. 在新网站支持Godaddy页面, owner: Hao
- 定义 menu/path mapping
- 定义通用路由
- pages/:id， id 是变量

- 例如，
- pages/home => home.html
- page/donate => donate.html

- 这样，多少页面都透过已处理，都没关系

## 3. 动态数据后端准备， owner: wangwentao,
- 数据库设计、实现；
- 给 前端 提供动态数据

## 4. 动态数据(公示）列表显示，view/template, owner: 伊迪Edie
- route: /information, /notice

## 5. 动态数据(公示）的准备, no owner yet
- 输入，编辑, preview,审核，发布
- 需要使用 Rich Text Editor 之类的

## 6. 用户登录, no owner yet
