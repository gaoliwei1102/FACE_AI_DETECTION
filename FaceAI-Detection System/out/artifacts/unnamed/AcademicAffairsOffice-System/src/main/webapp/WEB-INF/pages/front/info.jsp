<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + request.getContextPath() + "/";
%>
<html>
<head>
    <base href="<%=basePath%>">
    <meta charset="UTF-8">
    <link href="jquery/bootstrap_3.3.0/css/bootstrap.min.css" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="jquery/jquery-1.11.1-min.js"></script>
    <script type="text/javascript" src="jquery/bootstrap_3.3.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="panel panel-default">
    <div class="panel-heading">
        <div class="jumbotron">
            <p>AcademicAffairsOffice-教务处系统</p>
            <p>基于深度学习的在线课堂学生行为异常检测与分析系统(教务处端)</p>
        </div>
    </div>
    <div class="panel-body">
        <div class="page-header">
            <h1>学生端 </h1>
            <p>基于Python + PyQt5 + Mysql + BaiDu AI</p>
            <p><b>主要涉及以下功能:</b></p>
            <p>a)	人脸模拟检测  <br></p>
            <p>b)	查看同班同学<br></p>
            <p>c)	查看我的课表<br></p>
            <p>d)	查看我的违规<br></p>
            <p>e)	个人信息设置<br></p>
            <p>f)	课堂检测(待思考)<br></p>
            <p>g)	进行人脸注册<br></p>
            <p>i)	进行人脸删除<br></p>
            <p>j)	登录与退出<br></p>
    </div>


        <div class="page-header">
            <h1>教师端 </h1>
            <p>Python+PyQt5+Mysql</p>
            <p><b>主要涉及以下功能:</b></p>
            <p>a)	查看我的课程  <br></p>
            <p>b)	查看我的课程中违规学生<br></p>
            <p>c)	开辟新的课程<br></p>
            <p>d)	个人信息设置<br></p>
            <p>e)	登录和退出<br></p>
        </div>

        <div class="page-header">
            <h1>教务处 </h1>
            <p>Spring + SpringMVC + Mybatis + Bootstrap + Mysql</p>
            <p><b>主要涉及以下功能:</b></p>
            <p>a)	学生信息管理  <br></p>
            <p>b)	班级信息管理<br></p>
            <p>c)	教师信息管理<br></p>
            <p>d)	课程信息管理<br></p>
            <p>e)	违规信息管理<br></p>
            <p>f)	违规类型管理</p>
            <p>g)	个人设置</p>
        </div>


        <p>未完待续......</p>



    </div>
</body>
</html>