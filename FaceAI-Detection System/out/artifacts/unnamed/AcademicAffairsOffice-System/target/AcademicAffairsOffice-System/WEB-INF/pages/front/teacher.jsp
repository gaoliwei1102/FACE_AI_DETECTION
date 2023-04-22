<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + request.getContextPath() + "/";
%>
<html>
<head>
	<base href="<%=basePath%>">
<meta charset="UTF-8">

<link href="jquery/bootstrap_3.3.0/css/bootstrap.min.css" type="text/css" rel="stylesheet" />
<link href="jquery/bootstrap-datetimepicker-master/css/bootstrap-datetimepicker.min.css" type="text/css" rel="stylesheet" />
	<link href="jquery/bs_pagination-master/css/jquery.bs_pagination.min.css" type="text/css" rel="stylesheet" />

<script type="text/javascript" src="jquery/jquery-1.11.1-min.js"></script>
<script type="text/javascript" src="jquery/bootstrap_3.3.0/js/bootstrap.min.js"></script>
<script type="text/javascript" src="jquery/bootstrap-datetimepicker-master/js/bootstrap-datetimepicker.js"></script>
<script type="text/javascript" src="jquery/bootstrap-datetimepicker-master/locale/bootstrap-datetimepicker.zh-CN.js"></script>
	<script type="text/javascript" src="jquery/bs_pagination-master/js/jquery.bs_pagination.min.js"></script>
	<script type="text/javascript" src="jquery/bs_pagination-master/localization/en.js"></script>
<script type="text/javascript">

	$(function(){

		//点击搜索按钮按照指定条件进行搜索教师列表
		$("#selectTeachersByConditionForPageBtn").click(function () {
			selectTeachersByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
					$("#pagination").bs_pagination("getOption", "rowsPerPage"));
		});

		//用户点击全选按钮时，进行所有教师的全选或全不选
		$("#checkedAll").click(function () {
			$("#tbody input[type='checkbox']").prop("checked", this.checked);
		});

		//当教师点击单个教师选择时，若已全部选择，激活全选按钮，否则不激活
		$("#tbody").on("click", "input[type='checkbox']", function () {
			if($("#tbody input[type='checkbox']").size() == $("#tbody input[type='checkbox']:checked").size()){
				$("#checkedAll").prop("checked",true);
			}else {
				$("#checkedAll").prop("checked",false);
			}
		});

		//点击创建按钮的窗口弹出操作
		$("#addTeacherBtn").click(function () {
			//等待进行初始化操作
			$("#addTeacherForm").get(0).reset();
			$("#addModal").modal("show");
		});

		//点击保存按钮需要进行的操作
		$("#saveAddTeacherBtn").click(function () {

			var teacher_no = $("#add_teacher_teacher_no").val();
			var password = $("#add_teacher_password").val();
			var name = $("#add_teacher_name").val();
			var age = $("#add_teacher_age").val();
			var gender = $("#add_teacher_gender").val();
			var phone = $("#add_teacher_phone").val();
			var email = $("#add_teacher_email").val();

			if(teacher_no == ""){
				alert("请输入老师的编号!!!");
				return;
			}
			if(password == ""){
				alert("请输入老师的密钥!!!");
				return;
			}

			if(name == ""){
				alert("请输入老师的姓名!!!");
				return;
			}
			if(age == ""){
				alert("请输入老师的年龄!!!");
				return;
			}

			if(gender == ""){
				alert("请输入老师的性别!!!");
				return;
			}

			if(phone==""){
				alert("请输入老师的手机号!!!");
				return;
			}

			if (email==""){
				alert("请输入老师的邮箱!!!");
				return;
			}

			$.ajax({
				url:"front/teacher/addTeacher.do",
				data:{
					teacher_no:teacher_no,
					password:password,
					name:name,
					age:age,
					gender:gender,
					phone:phone,
					email:email,
				},
				type:'post',
				dataType:'json',
				success:function (data) {
					if(data.code=="1"){
						alert(data.message);
						$("#addModal").modal("hide");
						selectTeachersByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
								$("#pagination").bs_pagination("getOption", "rowsPerPage"));
					}else {
						alert(data.message);
						$("#addModal").modal("show");
					}
				}
			})
		});

		//打开更改教师信息的模态窗口
		$("#editTeacherBtn").click(function () {
			var editIds = $("tbody input[type='checkbox']:checked");
			if(editIds.size() == 0){
				alert("请选择具体的一个教师后，再进行修改操作!!!");
				return;
			}
			if(editIds.size() > 1){
				alert("最多只能选择一个教师，才能进行修改!!!");
				return;
			}

			var id = editIds[0].value;
			$.ajax({
				url:'front/teacher/queryTeacherById.do',
				data:{
					id:id
				},
				type:'post',
				dataType:'json',

				success:function (data) {
					$("#edit_id").val(data.id);
					$("#edit_teacher_teacher_no").val(data.teacherNo);
					$("#edit_teacher_password").val(data.password);
					$("#edit_teacher_name").val(data.name);
					$("#edit_teacher_age").val(data.age);
					$("#edit_teacher_gender").val(data.gender);
					$("#edit_teacher_phone").val(data.phone);
					$("#edit_teacher_email").val(data.email);

					$("#editModal").modal("show");

				}
			});

		});

		//保存更改的教师信息
		$("#saveEditTeacherBtn").click(function () {

			var id = $("#edit_id").val();
			var teacher_no = $("#edit_teacher_teacher_no").val();
			var password = $("#edit_teacher_password").val();
			var name = $("#edit_teacher_name").val();
			var age = $("#edit_teacher_age").val();
			var gender = $("#edit_teacher_gender").val();
			var phone = $("#edit_teacher_phone").val();
			var email = $("#edit_teacher_email").val();


			if(teacher_no == ""){
				alert("请输入老师的编号!!!");
				return;
			}
			if(password == ""){
				alert("请输入老师的密钥!!!");
				return;
			}
			if(name == ""){
				alert("请输入老师的姓名!!!");
				return;
			}
			if(age == ""){
				alert("请输入老师的年龄!!!");
				return;
			}

			if(gender == ""){
				alert("请输入老师的性别!!!");
				return;
			}

			if(phone==""){
				alert("请输入老师的手机号!!!");
				return;
			}

			if (email==""){
				alert("请输入老师的邮箱!!!");
				return;
			}


			$.ajax({
				url:'front/teacher/editTeacher.do',
				data:{
					id:id,
					teacher_no:teacher_no,
					password:password,
					name:name,
					age:age,
					gender:gender,
					phone:phone,
					email:email,
				},
				type:'post',
				dateType:'json',
				success:function (data) {
					if(data.code=="1"){
						alert(data.message);
						$("#editModal").modal("hide");
						selectTeachersByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
								$("#pagination").bs_pagination("getOption", "rowsPerPage"));
					}else {
						alert(data.message);
						$("#editModal").modal("show");
					}
				}
			})
		});


		//用户进行批量选择教师进行删除
		$("#deleteTeacherBtn").click(function () {
			var str = $("#tbody input[type='checkbox']:checked");
			if(str.size() == 0){
				alert("请先选择具体的教师, 再进行删除!!!");
				return;
			}
			if(window.confirm("已选中" + str.size() + "条数据, 确定删除吗?")){
				var ids = "";
				$.each(str, function (index, object) {
					ids += "id=" + this.value + "&";
				});
				ids = ids.substr(0, ids.length-1);
				$.ajax({
					url:"front/teacher/deleteTeacherByIds.do",
					data:ids,
					type:'post',
					dataType:'json',
					success:function (data) {
						if(data.code == "1"){
							alert(data.message);
							selectTeachersByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
									$("#pagination").bs_pagination("getOption", "rowsPerPage"));
						}else {
							alert(data.message);
						}
					}
				});
			}

		});


		//下载所有教师信息的xls文件
		$("#exportAllTeacherBtn").click(function () {
			window.location.href="front/teacher/downloadAllTeachers.do";
		});

		//显示所有
		$("#showAllTeachers").click(function () {
			$("#name").val("");
			selectTeachersByConditionForPage(1, 10);
		});

		//页面初始化操作，加载数据页
		selectTeachersByConditionForPage(1, 10);
	});
//

	//通过条件检索教师
	function selectTeachersByConditionForPage(beginNo, pageSize) {
		var name = $("#name").val();

		var beginNo = beginNo;
		var pageSize = pageSize;


		$.ajax({
			url:"front/teacher/queryAllTeachersByCondition.do",
			data: {
				name:name,
				beginNo:beginNo,
				pageSize:pageSize
			},
			type: 'post',
			dataType: 'json',
			success:function (data) {
				var strhtml = "";
				$.each(data, function (index, object) {
						strhtml += "<tr class=\"active\">";
						strhtml += "<td><input type=\"checkbox\" value=\""+ object.id + "\"/></td>";
						strhtml += "<td>"+ object.teacherNo +"</td>";
						strhtml += "<td>"+ object.password +"</td>";
						strhtml += "<td>"+ object.name +"</td>";
						strhtml += "<td>"+ object.age +"</td>";
						strhtml += "<td>"+ object.gender +"</td>";
						strhtml += "<td>"+object.phone+"</td>";
						strhtml += "<td>"+object.email+"</td>";
						strhtml += "</tr>";
				});
				$("#tbody").html(strhtml);

				$("#checkedAll").prop("checked", false);

				var total_page;
				if(data.counts%pageSize == 0){
					total_page = parseInt(data.counts/pageSize);
				}else {
					total_page = parseInt(data.counts/pageSize)+1;
				}


				$("#pagination").bs_pagination({
					currentPage:beginNo,
					rowsPerPage:pageSize,
					totalRows:data.counts,
					totalPages:total_page,

					visiblePageLinks: 5,

					showGoToPage: true,
					showRowsPerPage: true,
					showRowsInfo: true,

					onChangePage:function (event, pageObj) {
						selectTeachersByConditionForPage(pageObj.currentPage, pageObj.rowsPerPage);
					}
				})

			}
		})
	}

</script>
</head>
<body>

	<!-- 创建教师信息的模态窗口 -->
	<div class="modal fade" id="addModal" role="dialog">
		<div class="modal-dialog" role="document" style="width: 85%;">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">
						<span aria-hidden="true">×</span>
					</button>
					<h4 class="modal-title" id="myModalLabel1">创建教师信息</h4>
				</div>
				<div class="modal-body">
				
					<form class="form-horizontal" role="form" id="addTeacherForm">
						<div class="form-group">
							<label for="add_teacher_teacher_no" class="col-sm-2 control-label">编号<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" id="add_teacher_teacher_no" class="form-control">
							</div>
							<label for="add_teacher_password" class="col-sm-2 control-label">密码<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" class="form-control" id="add_teacher_password">
							</div>
						</div>

					
						<div class="form-group">
							<label for="add_teacher_name" class="col-sm-2 control-label">姓名<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" id="add_teacher_name" class="form-control">
							</div>
                            <label for="add_teacher_age" class="col-sm-2 control-label">年龄<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control" id="add_teacher_age">
                            </div>
						</div>
						
						<div class="form-group">
							<label for="add_teacher_gender" class="col-sm-2 control-label">性别</label>
							<div class="col-sm-10" style="width: 300px;">
								<select id="add_teacher_gender" class="form-control">
									<option value="男">男</option>
									<option value="女">女</option>
								</select>
							</div>
							<label for="add_teacher_phone" class="col-sm-2 control-label">电话</label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" class="form-control" id="add_teacher_phone" >
							</div>
						</div>
                        <div class="form-group">

                            <label for="add_teacher_email" class="col-sm-2 control-label">Email</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control" id="add_teacher_email">
                            </div>
                        </div>
						
					</form>
					
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
					<button type="button" class="btn btn-primary" id="saveAddTeacherBtn">保存</button>
				</div>
			</div>
		</div>
	</div>
	
	<!-- 修改教师信息的模态窗口 -->
	<div class="modal fade" id="editModal" role="dialog">
		<div class="modal-dialog" role="document" style="width: 85%;">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">
						<span aria-hidden="true">×</span>
					</button>
					<h4 class="modal-title" id="myModalLabel2">修改教师信息</h4>
				</div>
				<div class="modal-body">
				
					<form class="form-horizontal" role="form">
						<input type="hidden" id="edit_id">

						<div class="form-group">
							<label for="edit_teacher_teacher_no" class="col-sm-2 control-label">编号<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" id="edit_teacher_teacher_no" class="form-control">
							</div>
							<label for="edit_teacher_password" class="col-sm-2 control-label">密码<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" class="form-control" id="edit_teacher_password">
							</div>
						</div>


						<div class="form-group">
							<label for="edit_teacher_name" class="col-sm-2 control-label">姓名<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" id="edit_teacher_name" class="form-control">
							</div>
							<label for="edit_teacher_age" class="col-sm-2 control-label">年龄<span style="font-size: 15px; color: red;">*</span></label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" class="form-control" id="edit_teacher_age">
							</div>
						</div>

						<div class="form-group">
							<label for="edit_teacher_gender" class="col-sm-2 control-label">性别</label>
							<div class="col-sm-10" style="width: 300px;">
								<select id="edit_teacher_gender" class="form-control">
									<option value="男">男</option>
									<option value="女">女</option>
								</select>
							</div>
							<label for="edit_teacher_phone" class="col-sm-2 control-label">电话</label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" class="form-control" id="edit_teacher_phone" >
							</div>
						</div>
						<div class="form-group">

							<label for="edit_teacher_email" class="col-sm-2 control-label">Email</label>
							<div class="col-sm-10" style="width: 300px;">
								<input type="text" class="form-control" id="edit_teacher_email">
							</div>
						</div>
						
					</form>
					
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
					<button type="button" class="btn btn-primary" id="saveEditTeacherBtn">更新</button>
				</div>
			</div>
		</div>
	</div>

	
	
	<div>
		<div style="position: relative; left: 10px; top: -10px;">
			<div class="page-header">
				<h3>教师信息列表</h3>
			</div>
		</div>
	</div>
	<div style="position: relative; top: -20px; left: 0px; width: 100%; height: 100%;">
		<div style="width: 100%; position: absolute;top: 5px; left: 10px;">
		
			<div class="btn-toolbar" role="toolbar" style="height: 80px;">
				<form class="form-inline" role="form" style="position: relative;top: 8%; left: 5px;">
				  
				  <div class="form-group">
				    <div class="input-group">
				      <div class="input-group-addon">老师姓名</div>
				      <input class="form-control" type="text" id="name">
				    </div>
				  </div>
				  
				  <button type="button" class="btn btn-default" id="selectTeachersByConditionForPageBtn">查询</button>
				  
				</form>
			</div>
			<div class="btn-toolbar" role="toolbar" style="background-color: #F7F7F7; height: 50px; position: relative;top: 5px;">
				<div class="btn-group" style="position: relative; top: 18%;">
				  <button type="button" class="btn btn-primary" id="addTeacherBtn"><span class="glyphicon glyphicon-plus"></span> 创建</button>
				  <button type="button" class="btn btn-default" id="editTeacherBtn"><span class="glyphicon glyphicon-pencil"></span> 修改</button>
				  <button type="button" class="btn btn-danger"  id="deleteTeacherBtn"><span class="glyphicon glyphicon-minus"></span> 删除</button>
				</div>
				<div class="btn-group" style="position: relative; top: 18%;">
					<button id="showAllTeachers" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span> 显示所有 </button>
                    <button id="exportAllTeacherBtn" type="button" class="btn btn-default"><span class="glyphicon glyphicon-export"></span> 下载列表数据（批量导出）</button>

                </div>
			</div>
			<div style="position: relative;top: 10px;">
				<table class="table table-hover">
					<thead>
						<tr style="color: #B3B3B3;">
							<td><input type="checkbox" id="checkedAll"/></td>
							<td>编号</td>
							<td>密码</td>
							<td>姓名</td>
                            <td>年龄</td>
							<td>性别</td>
							<td>电话</td>
							<td>Email</td>
						</tr>
					</thead>
					<tbody id="tbody">

					</tbody>
				</table>
				<div id="pagination"></div>
			</div>
		</div>
		
	</div>
</body>
</html>