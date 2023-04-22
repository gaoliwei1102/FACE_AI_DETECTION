<%@ page import="com.gaoliwei.aaos.domain.Class" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + request.getContextPath() + "/";
    List<Class> classes = (List<Class>)request.getAttribute("classes");

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

            //点击搜索按钮按照指定条件进行搜索学生列表
            $("#selectStudentsByConditionForPageBtn").click(function () {
                selectStudentsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
            });

            //用户点击全选按钮时，进行所有学生的全选或全不选
            $("#checkedAll").click(function () {
                $("#tbody input[type='checkbox']").prop("checked", this.checked);
            });

            //当学生点击单个学生选择时，若已全部选择，激活全选按钮，否则不激活
            $("#tbody").on("click", "input[type='checkbox']", function () {
                if($("#tbody input[type='checkbox']").size() == $("#tbody input[type='checkbox']:checked").size()){
                    $("#checkedAll").prop("checked",true);
                }else {
                    $("#checkedAll").prop("checked",false);
                }
            });

            //点击创建按钮的窗口弹出操作
            $("#addStudentBtn").click(function () {
                //等待进行初始化操作
                $("#addStudentForm").get(0).reset();
                $("#addModal").modal("show");
            });

            //点击保存按钮需要进行的操作
            $("#saveAddStudentBtn").click(function () {

                var student_no = $("#add_student_student_no").val();
                var password = $("#add_student_password").val();
                var name = $("#add_student_name").val();
                var age = $("#add_student_age").val();
                var gender = $("#add_student_gender").val();
                var belong_class = $("#add_student_belong_class").val();
                var face_num = $("#add_student_face_num").val();



                if(student_no == ""){
                    alert("请输入学生的学号!!!");
                    return;
                }

                if(password == ""){
                    alert("请输入学生的密钥!!!");
                    return;
                }

                if(name == ""){
                    alert("请输入学生的姓名!!!");
                    return;
                }

                if(age == ""){
                    alert("请输入学生的年龄!!!");
                    return;
                }

                if (gender == ""){
                    alert("请输入学生的性别!!!");
                    return;
                }

                if (belong_class == ""){
                    alert("请输入学生所属的班级!!!");
                    return;
                }



                $.ajax({
                    url:"front/student/addStudent.do",
                    data:{
                        student_no:student_no,
                        password:password,
                        name:name,
                        age:age,
                        gender:gender,
                        belong_class:belong_class,
                        face_num:face_num,
                    },
                    type:'post',
                    dataType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#addModal").modal("hide");
                            selectStudentsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#addModal").modal("show");
                        }
                    }
                })
            });

            //打开更改学生信息的模态窗口
            $("#editStudentBtn").click(function () {
                var editIds = $("tbody input[type='checkbox']:checked");

                if(editIds.size() == 0){
                    alert("请选择具体的一个学生后，再进行修改操作!!!");
                    return;
                }
                if(editIds.size() > 1){
                    alert("最多只能选择一个学生，才能进行修改!!!");
                    return;
                }

                var id = editIds[0].value;
                $.ajax({
                    url:'front/student/queryStudentById.do',
                    data:{
                        id:id
                    },
                    type:'post',
                    dataType:'json',

                    success:function (data) {

                        $("#edit_id").val(data.id);
                        $("#edit_student_student_no").val(data.studentNo);
                        $("#edit_student_password").val(data.password);
                        $("#edit_student_name").val(data.name);
                        $("#edit_student_age").val(data.age);
                        $("#edit_student_gender").val(data.gender);
                        $("#edit_student_belong_class").val(data.belongClass);
                        $("#edit_student_face_num").val(data.faceNum);

                        $("#editModal").modal("show");

                    }
                });

            });

            //保存更改的学生信息
            $("#saveEditStudentBtn").click(function () {

                var id = $("#edit_id").val();
                var student_no = $("#edit_student_student_no").val();
                var password = $("#edit_student_password").val();
                var name = $("#edit_student_name").val();
                var age = $("#edit_student_age").val();
                var gender = $("#edit_student_gender").val();
                var belong_class = $("#edit_student_belong_class").val();
                var face_num = $("#edit_student_face_num").val();


                if(student_no == ""){
                    alert("请输入学生的学号!!!");
                    return;
                }

                if(password == ""){
                    alert("请输入学生的密钥!!!");
                    return;
                }

                if(name == ""){
                    alert("请输入学生的姓名!!!");
                    return;
                }

                if(age == ""){
                    alert("请输入学生的年龄!!!");
                    return;
                }

                if (gender == ""){
                    alert("请输入学生的性别!!!");
                    return;
                }

                if (belong_class == ""){
                    alert("请输入学生所属的班级!!!");
                    return;
                }

                $.ajax({
                    url:'front/student/editStudent.do',
                    data:{
                        id:id,
                        student_no:student_no,
                        password:password,
                        name:name,
                        age:age,
                        gender:gender,
                        belong_class:belong_class,
                        face_num:face_num,
                    },
                    type:'post',
                    dateType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#editModal").modal("hide");
                            selectStudentsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#editModal").modal("show");
                        }
                    }
                })
            });


            //用户进行批量选择学生进行删除
            $("#deleteStudentBtn").click(function () {
                var str = $("#tbody input[type='checkbox']:checked");
                if(str.size() == 0){
                    alert("请先选择具体的学生, 再进行删除!!!");
                    return;
                }
                if(window.confirm("已选中" + str.size() + "条数据, 确定删除吗?")){
                    var ids = "";
                    $.each(str, function (index, object) {
                        ids += "id=" + this.value + "&";
                    });
                    ids = ids.substr(0, ids.length-1);
                    $.ajax({
                        url:"front/student/deleteStudentByIds.do",
                        data:ids,
                        type:'post',
                        dataType:'json',
                        success:function (data) {
                            if(data.code == "1"){
                                alert(data.message);
                                selectStudentsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                            }else {
                                alert(data.message);
                            }
                        }
                    });
                }

            });


            //下载所有学生信息的xls文件
            $("#exportAllStudentBtn").click(function () {
                window.location.href="front/student/downloadAllStudents.do";
            });

            // 显示所有
            $("#showAllStudents").click(function () {
                $("#name").val("");
                selectStudentsByConditionForPage(1, 10);
            });

            //页面初始化操作，加载数据页
            selectStudentsByConditionForPage(1, 10);
        });


        //通过条件检索学生
        function selectStudentsByConditionForPage(beginNo, pageSize) {
            var name = $("#name").val();

            var beginNo = beginNo;
            var pageSize = pageSize;


            $.ajax({
                url:"front/student/queryAllStudentsByCondition.do",
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
                        strhtml += "<td>"+ object.studentNo +"</td>";
                        strhtml += "<td>"+ object.password +"</td>";
                        strhtml += "<td>"+ object.name +"</td>";
                        strhtml += "<td>"+object.gender+"</td>";
                        strhtml += "<td>"+object.age+"</td>";
                        strhtml += "<td>"+object.belongClass+"</td>";
                        strhtml += "<td>"+object.faceNum+"</td>";
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
                            selectStudentsByConditionForPage(pageObj.currentPage, pageObj.rowsPerPage);
                        }
                    })

                }
            })
        }

    </script>
</head>
<body>

<!-- 创建学生信息的模态窗口 -->
<div class="modal fade" id="addModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel1">创建学生信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form" id="addStudentForm">

                    <div class="form-group">
                        <label for="add_student_student_no" class="col-sm-2 control-label">学号<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="add_student_student_no" class="form-control">
                        </div>
                        <label for="add_student_password" class="col-sm-2 control-label">密钥<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="add_student_password">
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="add_student_name" class="col-sm-2 control-label">姓名</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="add_student_name" >
                        </div>

                        <label for="add_student_gender" class="col-sm-2 control-label">性别</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="add_student_gender" class="form-control">
                                <option value="男">男</option>
                                <option value="女">女</option>
                            </select>
                        </div>
                    </div>


                    <div class="form-group">

                        <label for="add_student_age" class="col-sm-2 control-label">年龄</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="add_student_age">
                        </div>

                        <label for="add_student_belong_class" class="col-sm-2 control-label">所属班级</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="add_student_belong_class" class="form-control">
                                <c:forEach items="${requestScope.classes}" var="clas" varStatus="status">
                                    <option value="${clas.id}">${clas.name}</option>
                                </c:forEach>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">

                        <label for="add_student_face_num" class="col-sm-2 control-label">人脸数量</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" value="0" class="form-control" id="add_student_face_num" readonly>
                        </div>


                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveAddStudentBtn">保存</button>
            </div>
        </div>
    </div>
</div>

<!-- 修改学生信息的模态窗口 -->
<div class="modal fade" id="editModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel2">修改学生信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form">
                    <input type="hidden" id="edit_id">
                    <div class="form-group">
                        <label for="edit_student_student_no" class="col-sm-2 control-label">学号<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="edit_student_student_no" class="form-control">
                        </div>
                        <label for="edit_student_password" class="col-sm-2 control-label">密钥<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="edit_student_password">
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="edit_student_name" class="col-sm-2 control-label">姓名</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="edit_student_name" >
                        </div>

                        <label for="edit_student_gender" class="col-sm-2 control-label">性别</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="edit_student_gender" class="form-control">
                                <option value="男">男</option>
                                <option value="女">女</option>
                            </select>
                        </div>
                    </div>


                    <div class="form-group">

                        <label for="edit_student_age" class="col-sm-2 control-label">年龄</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="edit_student_age">
                        </div>

                        <label for="edit_student_belong_class" class="col-sm-2 control-label">所属班级</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="edit_student_belong_class" class="form-control">
                                <c:forEach items="${requestScope.classes}" var="clas" varStatus="status">
                                    <option value="${clas.id}">${clas.name}</option>
                                </c:forEach>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">

                        <label for="edit_student_face_num" class="col-sm-2 control-label">人脸数量</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" value="0" class="form-control" id="edit_student_face_num" readonly>
                        </div>


                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveEditStudentBtn">更新</button>
            </div>
        </div>
    </div>
</div>



<div>
    <div style="position: relative; left: 10px; top: -10px;">
        <div class="page-header">
            <h3>学生信息列表</h3>
        </div>
    </div>
</div>
<div style="position: relative; top: -20px; left: 0px; width: 100%; height: 100%;">
    <div style="width: 100%; position: absolute;top: 5px; left: 10px;">

        <div class="btn-toolbar" role="toolbar" style="height: 80px;">
            <form class="form-inline" role="form" style="position: relative;top: 8%; left: 5px;">

                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-addon">学生姓名</div>
                        <input class="form-control" type="text" id="name">
                    </div>
                </div>

                <button type="button" class="btn btn-default" id="selectStudentsByConditionForPageBtn">查询</button>

            </form>
        </div>
        <div class="btn-toolbar" role="toolbar" style="background-color: #F7F7F7; height: 50px; position: relative;top: 5px;">
            <div class="btn-group" style="position: relative; top: 18%;">
                <button type="button" class="btn btn-primary" id="addStudentBtn"><span class="glyphicon glyphicon-plus"></span> 创建</button>
                <button type="button" class="btn btn-default" id="editStudentBtn"><span class="glyphicon glyphicon-pencil"></span> 修改</button>
                <button type="button" class="btn btn-danger"  id="deleteStudentBtn"><span class="glyphicon glyphicon-minus"></span> 删除</button>
            </div>
            <div class="btn-group" style="position: relative; top: 18%;">
                <button id="showAllStudents" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span> 显示所有 </button>
                <button id="exportAllStudentBtn" type="button" class="btn btn-default"><span class="glyphicon glyphicon-export"></span> 下载列表数据（批量导出）</button>

            </div>
        </div>
        <div style="position: relative;top: 10px;">
            <table class="table table-hover">
                <thead>
                <tr style="color: #B3B3B3;">
                    <td><input type="checkbox" id="checkedAll"/></td>
                    <td>学号</td>
                    <td>密钥</td>
                    <td>姓名</td>
                    <td>性别</td>
                    <td>年龄</td>
                    <td>所属班级</td>
                    <td>脸部数量</td>
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