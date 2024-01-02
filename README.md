#################################################
## Author-Ma tianyu
## Data 2024.1.2
#################################################

Flask Project Structure

-db
  -models.py
-app.py
-templates
  -.html
-static
  -css
  -js
-src
  

app.py
=======================================================
建立主页面路由：
  INDEX;
  DOWNLOAD;
  HELP；

提供服务器静态文件和图片资源

建立错误代码反馈页面


models.py
=======================================================

连接MySQL数据库；

对数据库中的Publish表进行ORM对象化；

定义函数，将ORM查询后返回的Query对象，转换为JSON格式返回



