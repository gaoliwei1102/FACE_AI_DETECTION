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

        $(function() {
            //通过日历让用户进行日期选择
            $(".mydate").datetimepicker({
                    language:'zh-CN',
                    format:"yyyy-mm-dd",
                    minView:'month',
                    initialDate:new Date(),
                    autoclose:true,
                    todayBtn:true
                });

            $(".time").datetimepicker({
                    language:'zh-CN',
                    format:'hh:ii',
                    startView:'hour',
                    initialDate:new Date(),
                    autoclose:true,
                    todayBtn:true,
                    theme: 'dark'
                });

            //点击搜索按钮按照指定条件进行搜索课程表列表
            $("#selectCoursesByConditionForPageBtn").click(function () {
                selectCoursesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
            });

            //用户点击全选按钮时，进行所有课程表的全选或全不选
            $("#checkedAll").click(function () {
                $("#tbody input[type='checkbox']").prop("checked", this.checked);
            });

            //当课程表点击单个课程表选择时，若已全部选择，激活全选按钮，否则不激活
            $("#tbody").on("click", "input[type='checkbox']", function () {
                if($("#tbody input[type='checkbox']").size() == $("#tbody input[type='checkbox']:checked").size()){
                    $("#checkedAll").prop("checked",true);
                }else {
                    $("#checkedAll").prop("checked",false);
                }
            });

            //点击创建按钮的窗口弹出操作
            $("#addCourseBtn").click(function () {
                //等待进行初始化操作
                $("#addCourseForm").get(0).reset();
                $("#addModal").modal("show");
            });

            //点击保存按钮需要进行的操作
            $("#saveAddCourseBtn").click(function () {

                var subject = $("#add_course_subject").val();
                var teacher = $("#add_course_teacher").val();
                var tbl_class = $("#add_course_tbl_class").val();
                var start_day = $("#add_course_start_day").val();
                var start_time = $("#add_course_start_time").val();
                var end_time = $("#add_course_end_time").val();
                var remarks = $("#add_course_remarks").val();



                if(subject == ""){
                    alert("请输入课程的科目!!!");
                    return;
                }

                if(teacher == ""){
                    alert("请输入课程的老师!!!");
                    return;
                }

                if(tbl_class == ""){
                    alert("请输入课程的班级!!!");
                    return;
                }

                if(start_day == ""){
                    alert("请输入课程的日期!!!");
                    return;
                }

                if (start_time == ""){
                    alert("请输入课程的开始时间!!!");
                    return;
                }

                if (end_time == ""){
                    alert("请输入课程的结束时间!!!");
                    return;
                }

                if (remarks == ""){
                    alert("请输入课程的备注!!!");
                    return;
                }



                $.ajax({
                    url:"front/course/addCourse.do",
                    data:{
                        subject:subject,
                        teacher:teacher,
                        tbl_class:tbl_class,
                        start_day:start_day,
                        start_time:start_time,
                        end_time:end_time,
                        remarks:remarks,
                    },
                    type:'post',
                    dataType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#addModal").modal("hide");
                            selectCoursesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#addModal").modal("show");
                        }
                    }
                })
            });

            //打开更改课程表信息的模态窗口
            $("#editCourseBtn").click(function () {
                var editIds = $("tbody input[type='checkbox']:checked");

                if(editIds.size() == 0){
                    alert("请选择具体的一个课程表后，再进行修改操作!!!");
                    return;
                }
                if(editIds.size() > 1){
                    alert("最多只能选择一个课程表，才能进行修改!!!");
                    return;
                }

                var id = editIds[0].value;
                $.ajax({
                    url:'front/course/queryCourseById.do',
                    data:{
                        id:id
                    },
                    type:'post',
                    dataType:'json',

                    success:function (data) {

                        $("#edit_id").val(data.id);
                        $("#edit_course_subject").val(data.subject);
                        $("#edit_course_teacher").val(data.teacher);
                        $("#edit_course_tbl_class").val(data.tblClass);
                        $("#edit_course_start_day").val(data.startDay);
                        $("#edit_course_start_time").val(data.startTime);
                        $("#edit_course_end_time").val(data.endTime);
                        $("#edit_course_remarks").val(data.remarks);

                        $("#editModal").modal("show");

                    }
                });

            });

            //保存更改的课程表信息
            $("#saveEditCourseBtn").click(function () {

                var id = $("#edit_id").val();
                var subject = $("#edit_course_subject").val();
                var teacher = $("#edit_course_teacher").val();
                var tbl_class = $("#edit_course_tbl_class").val();
                var start_day = $("#edit_course_start_day").val();
                var start_time = $("#edit_course_start_time").val();
                var end_time = $("#edit_course_end_time").val();
                var remarks = $("#edit_course_remarks").val();


                if(subject == ""){
                    alert("请输入课程的科目!!!");
                    return;
                }

                if(teacher == ""){
                    alert("请输入课程的老师!!!");
                    return;
                }

                if(tbl_class == ""){
                    alert("请输入课程的班级!!!");
                    return;
                }

                if(start_day == ""){
                    alert("请输入课程的日期!!!");
                    return;
                }

                if (start_time == ""){
                    alert("请输入课程的开始时间!!!");
                    return;
                }

                if (end_time == ""){
                    alert("请输入课程的结束时间!!!");
                    return;
                }

                if (remarks == ""){
                    alert("请输入课程的备注!!!");
                    return;
                }

                $.ajax({
                    url:'front/course/editCourse.do',
                    data:{
                        id:id,
                        subject:subject,
                        teacher:teacher,
                        tbl_class:tbl_class,
                        start_day:start_day,
                        start_time:start_time,
                        end_time:end_time,
                        remarks:remarks,
                    },
                    type:'post',
                    dateType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#editModal").modal("hide");
                            selectCoursesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#editModal").modal("show");
                        }
                    }
                })
            });


            //用户进行批量选择课程表进行删除
            $("#deleteCourseBtn").click(function () {
                var str = $("#tbody input[type='checkbox']:checked");
                if(str.size() == 0){
                    alert("请先选择具体的课程表, 再进行删除!!!");
                    return;
                }
                if(window.confirm("已选中" + str.size() + "条数据, 确定删除吗?")){
                    var ids = "";
                    $.each(str, function (index, object) {
                        ids += "id=" + this.value + "&";
                    });
                    ids = ids.substr(0, ids.length-1);
                    $.ajax({
                        url:"front/course/deleteCourseByIds.do",
                        data:ids,
                        type:'post',
                        dataType:'json',
                        success:function (data) {
                            if(data.code == "1"){
                                alert(data.message);
                                selectCoursesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                            }else {
                                alert(data.message);
                            }
                        }
                    });
                }

            });

            //下载所有课程表信息的xls文件
            $("#exportAllCourseBtn").click(function () {
                window.location.href="front/course/downloadAllCourses.do";
            });

            // 显示所有
            $("#showAllCourses").click(function () {
                $("#name").val("");
                selectCoursesByConditionForPage(1, 10);
            });

            //页面初始化操作，加载数据页
            selectCoursesByConditionForPage(1, 10);
        });


            //通过条件检索课程表
            function selectCoursesByConditionForPage(beginNo, pageSize) {
                var name = $("#name").val();

                var beginNo = beginNo;
                var pageSize = pageSize;


                $.ajax({
                    url: "front/course/queryAllCoursesByCondition.do",
                    data: {
                        name: name,
                        beginNo: beginNo,
                        pageSize: pageSize
                    },
                    type: 'post',
                    dataType: 'json',
                    success: function (data) {
                        var strhtml = "";
                        $.each(data, function (index, object) {
                            strhtml += "<tr class=\"active\">";
                            strhtml += "<td><input type=\"checkbox\" value=\"" + object.id + "\"/></td>";
                            strhtml += "<td>" + object.subject + "</td>";
                            strhtml += "<td>" + object.teacher + "</td>";
                            strhtml += "<td>" + object.tblClass + "</td>";
                            strhtml += "<td>" + object.startDay + "</td>";
                            strhtml += "<td>" + object.startTime + "</td>";
                            strhtml += "<td>" + object.endTime + "</td>";
                            strhtml += "<td>" + object.remarks + "</td>";
                            strhtml += "</tr>";
                        });
                        $("#tbody").html(strhtml);

                        $("#checkedAll").prop("checked", false);

                        var total_page;
                        if (data.counts % pageSize == 0) {
                            total_page = parseInt(data.counts / pageSize);
                        } else {
                            total_page = parseInt(data.counts / pageSize) + 1;
                        }


                        $("#pagination").bs_pagination({
                            currentPage: beginNo,
                            rowsPerPage: pageSize,
                            totalRows: data.counts,
                            totalPages: total_page,

                            visiblePageLinks: 5,

                            showGoToPage: true,
                            showRowsPerPage: true,
                            showRowsInfo: true,

                            onChangePage: function (event, pageObj) {
                                selectCoursesByConditionForPage(pageObj.currentPage, pageObj.rowsPerPage);
                            }
                        })

                    }
                })
            }

    </script>
</head>
<body>

    <!-- 创建课程表信息的模态窗口 -->
    <div class="modal fade" id="addModal" role="dialog">
        <div class="modal-dialog" role="document" style="width: 85%;">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">
                        <span aria-hidden="true">×</span>
                    </button>
                    <h4 class="modal-title" id="myModalLabel1">创建课程表信息</h4>
                </div>
                <div class="modal-body">

                    <form class="form-horizontal" role="form" id="addCourseForm">

                        <div class="form-group">
                            <label for="add_course_subject" class="col-sm-2 control-label">科目<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <select id="add_course_subject" class="form-control">
                                    <c:forEach items="${requestScope.subjects}" var="subject" varStatus="status">
                                        <option value="${subject.id}">${subject.name}</option>
                                    </c:forEach>
                                </select>
                            </div>
                            <label for="add_course_tbl_class" class="col-sm-2 control-label">班级<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <select id="add_course_tbl_class" class="form-control">
                                    <c:forEach items="${requestScope.classes}" var="clas" varStatus="status">
                                        <option value="${clas.id}">${clas.name}</option>
                                    </c:forEach>
                                </select>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="add_course_teacher" class="col-sm-2 control-label">老师<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <select id="add_course_teacher" class="form-control">
                                    <c:forEach items="${requestScope.teachers}" var="teacher" varStatus="status">
                                        <option value="${teacher.id}">${teacher.name}</option>
                                    </c:forEach>
                                </select>
                            </div>

                            <label for="add_course_start_day" class="col-sm-2 control-label">课程日期</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control mydate" id="add_course_start_day" readonly>
                            </div>
                        </div>

                        <div class="form-group">

                            <label for="add_course_start_time" class="col-sm-2 control-label">开始时间</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control time" id="add_course_start_time" readonly>
                            </div>
                            <label for="add_course_end_time" class="col-sm-2 control-label">结束时间</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control time" id="add_course_end_time" readonly>
                            </div>

                        </div>

                        <div class="form-group">
                            <label for="add_course_remarks" class="col-sm-2 control-label">备注<span style="font-size: 15px; color: red;"></span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <textarea type="text" id="add_course_remarks" class="form-control"></textarea>
                            </div>
                        </div>


                    </form>

                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                    <button type="button" class="btn btn-primary" id="saveAddCourseBtn">保存</button>
                </div>
            </div>
        </div>
    </div>

    <!-- 修改课程表信息的模态窗口 -->
    <div class="modal fade" id="editModal" role="dialog">
        <div class="modal-dialog" role="document" style="width: 85%;">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">
                        <span aria-hidden="true">×</span>
                    </button>
                    <h4 class="modal-title" id="myModalLabel2">修改课程表信息</h4>
                </div>
                <div class="modal-body">

                    <form class="form-horizontal" role="form">
                        <input type="hidden" id="edit_id">
                        <div class="form-group">
                            <label for="edit_course_subject" class="col-sm-2 control-label">科目<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <select id="edit_course_subject" class="form-control">
                                    <c:forEach items="${requestScope.subjects}" var="subject" varStatus="status">
                                        <option value="${subject.id}">${subject.name}</option>
                                    </c:forEach>
                                </select>
                            </div>
                            <label for="edit_course_tbl_class" class="col-sm-2 control-label">班级<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <select id="edit_course_tbl_class" class="form-control">
                                    <c:forEach items="${requestScope.classes}" var="clas" varStatus="status">
                                        <option value="${clas.id}">${clas.name}</option>
                                    </c:forEach>
                                </select>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="edit_course_teacher" class="col-sm-2 control-label">老师<span style="font-size: 15px; color: red;">*</span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <select id="edit_course_teacher" class="form-control">
                                    <c:forEach items="${requestScope.teachers}" var="teacher" varStatus="status">
                                        <option value="${teacher.id}">${teacher.name}</option>
                                    </c:forEach>
                                </select>
                            </div>

                            <label for="edit_course_start_day" class="col-sm-2 control-label">课程日期</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control mydate" id="edit_course_start_day" readonly>
                            </div>
                        </div>

                        <div class="form-group">

                            <label for="edit_course_start_time" class="col-sm-2 control-label">开始时间</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control time" id="edit_course_start_time" readonly>
                            </div>
                            <label for="edit_course_end_time" class="col-sm-2 control-label">结束时间</label>
                            <div class="col-sm-10" style="width: 300px;">
                                <input type="text" class="form-control time" id="edit_course_end_time" readonly>
                            </div>

                        </div>

                        <div class="form-group">
                            <label for="edit_course_remarks" class="col-sm-2 control-label">备注<span style="font-size: 15px; color: red;"></span></label>
                            <div class="col-sm-10" style="width: 300px;">
                                <textarea type="text" id="edit_course_remarks" class="form-control"></textarea>
                            </div>
                        </div>

                    </form>

                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                    <button type="button" class="btn btn-primary" id="saveEditCourseBtn">更新</button>
                </div>
            </div>
        </div>
    </div>



    <div>
        <div style="position: relative; left: 10px; top: -10px;">
            <div class="page-header">
                <h3>课程表信息列表</h3>
            </div>
        </div>
    </div>
    <div style="position: relative; top: -20px; left: 0px; width: 100%; height: 100%;">
        <div style="width: 100%; position: absolute;top: 5px; left: 10px;">

            <div class="btn-toolbar" role="toolbar" style="height: 80px;">
                <form class="form-inline" role="form" style="position: relative;top: 8%; left: 5px;">

                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-addon">课程名称</div>
                            <input class="form-control" type="text" id="name">
                        </div>
                    </div>

                    <button type="button" class="btn btn-default" id="selectCoursesByConditionForPageBtn">查询</button>

                </form>
            </div>
            <div class="btn-toolbar" role="toolbar" style="background-color: #F7F7F7; height: 50px; position: relative;top: 5px;">
                <div class="btn-group" style="position: relative; top: 18%;">
                    <button type="button" class="btn btn-primary" id="addCourseBtn"><span class="glyphicon glyphicon-plus"></span> 创建</button>
                    <button type="button" class="btn btn-default" id="editCourseBtn"><span class="glyphicon glyphicon-pencil"></span> 修改</button>
                    <button type="button" class="btn btn-danger"  id="deleteCourseBtn"><span class="glyphicon glyphicon-minus"></span> 删除</button>
                </div>
                <div class="btn-group" style="position: relative; top: 18%;">
                    <button id="showAllCourses" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span> 显示所有 </button>
                    <button id="exportAllCourseBtn" type="button" class="btn btn-default"><span class="glyphicon glyphicon-export"></span> 下载列表数据（批量导出）</button>

                </div>
            </div>
            <div style="position: relative;top: 10px;">
                <table class="table table-hover">
                    <thead>
                    <tr style="color: #B3B3B3;">
                        <td><input type="checkbox" id="checkedAll"/></td>
                        <td>学科</td>
                        <td>老师</td>
                        <td>班级</td>
                        <td>日期</td>
                        <td>开始时间</td>
                        <td>结束时间</td>
                        <td>备注</td>
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