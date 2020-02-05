# 技术框架
- 后端：Python Flask
- 前端：Server Rendering + Bootstrap + jQuery
- 数据库：PostgreSQL

# 下一步的技术分工：

##More pages:
### 主页，校友活动，武汉疫情动态，校友会在行动， owner: Hao
### 捐赠方式和公示，联系我们，Q&A: 古道西风


## 动态数据后端准备， owner: wangwentao,
- 数据库设计、实现；
- 给 前端 提供动态数据
## 用户登录,  owner: wangwentao
- 登录界面
- 认证

## 动态数据(公示）列表显示， owner: Aya/伊迪Edie
- /notices
- /admin/notices

## 动态数据(公示）输入、编辑, owner: Aya
- 输入，编辑, preview,审核，发布
- 需要使用 Rich Text Editor 之类的

## Google Analytice: owner: 唯唯安
## 美图， owner: QRN, 孟鹏秋, 大游侠
## 网页信息的收集、整理、审核和验证， 周广宇Gavin

# Done
## Godaddy 网站迁移， owner: @robyy
- https://sites.google.com/view/wuhan-ncov-crisis-fundraise/home
- 把Godaddy网站上的网页，下了载下来，整理一下
- 放到我们的source code 的目录下面 pages
- 做为静态页面
## 在新网站支持Godaddy页面, owner: Hao
- 定义 menu/path mapping
- 定义通用路由
- pages/:id， id 是变量
- 例如，
- pages/home => home.html
- page/donate => donate.html
- 这样，多少页面都透过已处理，都没关系
# Index page， Hao
## Deployment
- Deployment code, owner: wangwentao
- Daily Deploy, owner: wangwentao, Hao
## Donate page: Gaohong Wei
## Notice news page: 伊迪Edie/Gaohong Wei



