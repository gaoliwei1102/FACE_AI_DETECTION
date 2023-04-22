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
<script type="text/javascript">
	$(function () {
		$(window).keydown(function (e) {
			if(e.keyCode == 13){
				$("#login_btn").click();
			}
		});


		$("#login_btn").click(function () {
			var loginAct = $.trim($("#login_act").val());
			var loginPwd = $.trim($("#login_pwd").val());

			if(loginAct == "" | loginPwd == ""){
				alert("账号或密码不可以为空，请重新输入!!!")
			}

			$.ajax({
				url:'front/login/MatchAdmins.do',
				data:{
					username:loginAct,
					password:loginPwd
				},
				type:'post',
				dataType:'json',
				success:function (data) {
					if(data.code == '1'){
						window.location.href="front/index/gotoIndex.do";
					}else {
						$("#msg").text("账号密码不正确，请重试!");
					}
				},
				beforeSend:function () {
					$("#msg").text("正在验证中......");
					return true;
				}
			})
		});
	});
</script>
</head>
<body>
	<div style="position: absolute; top: 0px; left: 0px; width: 60%;">
		<img src="image/IMG_7114.JPG" style="width: 100%; height: 90%; position: relative; top: 50px;">
	</div>
	<div id="top" style="height: 50px; background-color: #3C3C3C; width: 100%;">
		<div style="position: absolute; top: 5px; left: 0px; font-size: 30px; font-weight: 400; color: white; font-family: 'times new roman'">AcademicAffairsOffice &nbsp;<span style="font-size: 12px;">&copy;2022&nbsp;教务系统</span></div>
	</div>
	
	<div style="position: absolute; top: 120px; right: 100px;width:450px;height:400px;border:1px solid #D5D5D5">
		<div style="position: absolute; top: 0px; right: 60px;">
			<div class="page-header">
				<h1>登录</h1>
			</div>
			<form action="../workbench/index.html" class="form-horizontal" role="form">
				<div class="form-group form-group-lg">
					<div style="width: 350px;">
						<input class="form-control" id="login_act" type="text" placeholder="用户名">
					</div>
					<div style="width: 350px; position: relative;top: 20px;">
						<input class="form-control" id="login_pwd" type="password" placeholder="密码">
					</div>
					<div class="checkbox"  style="position: relative;top: 30px; left: 10px;">

						<span id="msg">暂不支持注册哈</span>
					</div>
					<button type="button" id="login_btn" class="btn btn-primary btn-lg btn-block"  style="width: 350px; position: relative;top: 45px;">登录</button>
				</div>
			</form>
		</div>
	</div>
</body>
</html>