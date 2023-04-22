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

            //点击搜索按钮按照指定条件进行搜索违规列表
            $("#selectViolatesByConditionForPageBtn").click(function () {
                selectViolatesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
            });

            //用户点击全选按钮时，进行所有违规的全选或全不选
            $("#checkedAll").click(function () {
                $("#tbody input[type='checkbox']").prop("checked", this.checked);
            });

            //当违规点击单个违规选择时，若已全部选择，激活全选按钮，否则不激活
            $("#tbody").on("click", "input[type='checkbox']", function () {
                if($("#tbody input[type='checkbox']").size() == $("#tbody input[type='checkbox']:checked").size()){
                    $("#checkedAll").prop("checked",true);
                }else {
                    $("#checkedAll").prop("checked",false);
                }
            });


            //打开更改违规信息的模态窗口
            $("#editViolateBtn").click(function () {
                var editIds = $("tbody input[type='checkbox']:checked");
                if(editIds.size() == 0){
                    alert("请选择具体的一个违规后，再进行修改操作!!!");
                    return;
                }
                if(editIds.size() > 1){
                    alert("最多只能选择一个违规，才能进行修改!!!");
                    return;
                }

                var id = editIds[0].value;
                $.ajax({
                    url:'front/violate/queryViolateById.do',
                    data:{
                        id:id
                    },
                    type:'post',
                    dataType:'json',

                    success:function (data) {

                        var violate = data['violate'];
                        var students = data['students'];

                        str_html = "";
                        for(var i=0; i < students.length; i++){
                            str_html += "<option value=" + students[i].id +">" + students[i].name + "</option>";
                        }

                        $("#edit_violate_student").html(str_html);

                        $("#edit_id").val(violate.id);
                        $("#edit_violate_course").val(violate.course);
                        $("#edit_violate_type").val(violate.type);
                        $("#edit_violate_student").val(violate.student);
                        $("#edit_violate_remarks").val(violate.remarks);

                        $("#editModal").modal("show");

                    }
                });

            });

            //保存更改的违规信息
            $("#saveEditViolateBtn").click(function () {

                var id = $("#edit_id").val();
                var course = $("#edit_violate_course").val();
                var type = $("#edit_violate_type").val();
                var student = $("#edit_violate_student").val();
                var remarks = $("#edit_violate_remarks").val();


                if(type == ""){
                    alert("请输入违规的类型!!!");
                    return;
                }
                if(course == ""){
                    alert("请输入违规的课程!!!");
                    return;
                }
                if(student == ""){
                    alert("请输入违规的学生!!!");
                    return;
                }
                if(remarks == ""){
                    alert("请输入违规的备注!!!");
                    return;
                }

                $.ajax({
                    url:'front/violate/editViolate.do',
                    data:{
                        id:id,
                        course:course,
                        type:type,
                        student:student,
                        remarks:remarks,
                    },
                    type:'post',
                    dateType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#editModal").modal("hide");
                            selectViolatesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#editModal").modal("show");
                        }
                    }
                })
            });


            //用户进行批量选择违规进行删除
            $("#deleteViolateBtn").click(function () {
                var str = $("#tbody input[type='checkbox']:checked");
                if(str.size() == 0){
                    alert("请先选择具体的违规, 再进行删除!!!");
                    return;
                }
                if(window.confirm("已选中" + str.size() + "条数据, 确定删除吗?")){
                    var ids = "";
                    $.each(str, function (index, object) {
                        ids += "id=" + this.value + "&";
                    });
                    ids = ids.substr(0, ids.length-1);
                    $.ajax({
                        url:"front/violate/deleteViolateByIds.do",
                        data:ids,
                        type:'post',
                        dataType:'json',
                        success:function (data) {
                            if(data.code == "1"){
                                alert(data.message);
                                selectViolatesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                            }else {
                                alert(data.message);
                            }
                        }
                    });
                }

            });


            //下载所有违规信息的xls文件
            $("#exportAllViolateBtn").click(function () {
                window.location.href="front/violate/downloadAllViolates.do";
            });

            //显示所有
            $("#showAllViolates").click(function () {
                $("#name").val("");
                selectViolatesByConditionForPage(1, 10);
            });

            //页面初始化操作，加载数据页
            selectViolatesByConditionForPage(1, 10);
        });
        //

        //通过条件检索违规
        function selectViolatesByConditionForPage(beginNo, pageSize) {
            var name = $("#name").val();

            var beginNo = beginNo;
            var pageSize = pageSize;


            $.ajax({
                url:"front/violate/queryAllViolatesByCondition.do",
                data: {
                    name:name,
                    beginNo:beginNo,
                    pageSize:pageSize
                },
                type: 'post',
                dataType: 'json',
                success:function (data) {
                    var violates = data['violates'];
                    var courses = data['courses'];
                    var teachers = data['teachers'];
                    var subjects = data['subjects'];
                    var classes = data['classes'];
                    var strhtml = "";

                    for (var i = 0; i < violates.length; i++){
                        strhtml += "<tr class=\"active\">";
                        strhtml += "<td><input type=\"checkbox\" value=\""+ violates[i].id + "\"/></td>";
                        strhtml += "<td>"+ violates[i].type +"</td>";
                        strhtml += "<td>"+ violates[i].student +"</td>";
                        strhtml += "<td>"+ classes[i].name +"</td>";
                        strhtml += "<td>"+ subjects[i].name +"</td>";
                        strhtml += "<td>"+ teachers[i].name +"</td>";
                        strhtml += "<td>"+ courses[i].startDay +"</td>";
                        strhtml += "<td>"+ courses[i].startTime +"</td>";
                        strhtml += "<td>"+ courses[i].endTime +"</td>";
                        strhtml += "<td>"+ violates[i].remarks +"</td>";
                        strhtml += "<td>"+violates[i].createTime+"</td>";
                        strhtml += "</tr>";
                    }

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
                            selectViolatesByConditionForPage(pageObj.currentPage, pageObj.rowsPerPage);
                        }
                    })

                }
            })
        }

    </script>
</head>
<body>


<!-- 修改违规信息的模态窗口 -->
<div class="modal fade" id="editModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel2">修改违规信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form">

                    <div class="form-group">
                        <label for="edit_id" class="col-sm-2 control-label">违规ID</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="edit_id" class="form-control" readonly>
                        </div>
                        <label for="edit_violate_course" class="col-sm-2 control-label">班级ID</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="edit_violate_course" class="form-control" readonly>
                        </div>


                    </div>


                    <div class="form-group">
                        <label for="edit_violate_type" class="col-sm-2 control-label">违规名称<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="edit_violate_type" class="form-control">
                                <c:forEach items="${requestScope.violateTypes}" var="violateType" varStatus="status">
                                    <option value="${violateType.id}">${violateType.name}</option>
                                </c:forEach>
                            </select>
                        </div>
                        <label for="edit_violate_student" class="col-sm-2 control-label">学生姓名<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="edit_violate_student" class="form-control">
                                <c:forEach items="${requestScope.students}" var="student" varStatus="status">
                                    <option value="${student.id}">${student.name}</option>
                                </c:forEach>
                            </select>
                        </div>

                    </div>


                    <div class="form-group">

                        <label for="edit_violate_remarks" class="col-sm-2 control-label">备注</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="edit_violate_remarks" class="form-control">
                        </div>
                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveEditViolateBtn">更新</button>
            </div>
        </div>
    </div>
</div>



<div>
    <div style="position: relative; left: 10px; top: -10px;">
        <div class="page-header">
            <h3>违规信息列表</h3>
        </div>
    </div>
</div>
<div style="position: relative; top: -20px; left: 0px; width: 100%; height: 100%;">
    <div style="width: 100%; position: absolute;top: 5px; left: 10px;">

        <div class="btn-toolbar" role="toolbar" style="height: 80px;">
            <form class="form-inline" role="form" style="position: relative;top: 8%; left: 5px;">

                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-addon">违规名称</div>
                        <input class="form-control" type="text" id="name">
                    </div>
                </div>

                <button type="button" class="btn btn-default" id="selectViolatesByConditionForPageBtn">查询</button>

            </form>
        </div>
        <div class="btn-toolbar" role="toolbar" style="background-color: #F7F7F7; height: 50px; position: relative;top: 5px;">
            <div class="btn-group" style="position: relative; top: 18%;">
                <button type="button" class="btn btn-default" id="editViolateBtn"><span class="glyphicon glyphicon-pencil"></span> 修改</button>
                <button type="button" class="btn btn-danger"  id="deleteViolateBtn"><span class="glyphicon glyphicon-minus"></span> 删除</button>
            </div>
            <div class="btn-group" style="position: relative; top: 18%;">
                <button id="showAllViolates" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span> 显示所有 </button>
                <button id="exportAllViolateBtn" type="button" class="btn btn-default"><span class="glyphicon glyphicon-export"></span> 下载列表数据（批量导出）</button>

            </div>
        </div>
        <div style="position: relative;top: 10px;">
            <table class="table table-hover">
                <thead>
                <tr style="color: #B3B3B3;">
                    <td><input type="checkbox" id="checkedAll"/></td>
                    <td>违规名称</td>
                    <td>学生姓名</td>
                    <td>所属班级</td>
                    <td>课程名称</td>
                    <td>授课老师</td>
                    <td>课程日期</td>
                    <td>开始时间</td>
                    <td>结束时间</td>
                    <td>备注</td>
                    <td>创建时间</td>
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
