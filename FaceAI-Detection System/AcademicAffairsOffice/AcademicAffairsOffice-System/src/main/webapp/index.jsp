<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + request.getContextPath() + "/";
%>
<html>
<head>
    <base href="<%=basePath%>">
    <script type="text/javascript">
        window.location.href="front/login/gotoLoginIndex.do"
    </script>
</head>
<html>
<body>
</body>
</html>
