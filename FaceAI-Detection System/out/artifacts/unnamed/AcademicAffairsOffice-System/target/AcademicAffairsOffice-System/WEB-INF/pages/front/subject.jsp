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

            //点击搜索按钮按照指定条件进行搜索科目列表
            $("#selectSubjectsByConditionForPageBtn").click(function () {
                selectSubjectsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
            });

            //用户点击全选按钮时，进行所有科目的全选或全不选
            $("#checkedAll").click(function () {
                $("#tbody input[type='checkbox']").prop("checked", this.checked);
            });

            //当科目点击单个科目选择时，若已全部选择，激活全选按钮，否则不激活
            $("#tbody").on("click", "input[type='checkbox']", function () {
                if($("#tbody input[type='checkbox']").size() == $("#tbody input[type='checkbox']:checked").size()){
                    $("#checkedAll").prop("checked",true);
                }else {
                    $("#checkedAll").prop("checked",false);
                }
            });

            //点击创建按钮的窗口弹出操作
            $("#addSubjectBtn").click(function () {
                //等待进行初始化操作
                $("#addSubjectForm").get(0).reset();
                $("#addModal").modal("show");
            });

            //点击保存按钮需要进行的操作
            $("#saveAddSubjectBtn").click(function () {

                var name = $("#add_subject_name").val();
                var information = $("#add_subject_information").val();
                var score = $("#add_subject_score").val();


                if(name == ""){
                    alert("请输入科目的名称!!!");
                    return;
                }
                if(score == ""){
                    alert("请输入科目的学分!!!");
                    return;
                }

                if(information == ""){
                    alert("请输入科目的详细信息!!!");
                    return;
                }


                $.ajax({
                    url:"front/subject/addSubject.do",
                    data:{
                        name:name,
                        information:information,
                        score:score,
                    },
                    type:'post',
                    dataType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#addModal").modal("hide");
                            selectSubjectsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#addModal").modal("show");
                        }
                    }
                })
            });

            //打开更改科目信息的模态窗口
            $("#editSubjectBtn").click(function () {
                var editIds = $("tbody input[type='checkbox']:checked");
                if(editIds.size() == 0){
                    alert("请选择具体的一个科目后，再进行修改操作!!!");
                    return;
                }
                if(editIds.size() > 1){
                    alert("最多只能选择一个科目，才能进行修改!!!");
                    return;
                }

                var id = editIds[0].value;
                $.ajax({
                    url:'front/subject/querySubjectById.do',
                    data:{
                        id:id
                    },
                    type:'post',
                    dataType:'json',

                    success:function (data) {
                        $("#edit_id").val(data.id);
                        $("#edit_subject_name").val(data.name);
                        $("#edit_subject_score").val(data.score);
                        $("#edit_subject_information").val(data.information);



                        $("#editModal").modal("show");

                    }
                });

            });

            //保存更改的科目信息
            $("#saveEditSubjectBtn").click(function () {

                var id = $("#edit_id").val();
                var name = $("#edit_subject_name").val();
                var score = $("#edit_subject_score").val();
                var information = $("#edit_subject_information").val();


                if(name == ""){
                    alert("请输入科目的名称!!!");
                    return;
                }
                if(score == ""){
                    alert("请输入科目的学分!!!");
                    return;
                }

                if(information == ""){
                    alert("请输入科目的详细信息!!!");
                    return;
                }


                $.ajax({
                    url:'front/subject/editSubject.do',
                    data:{
                        id:id,
                        name:name,
                        information:information,
                        score:score,
                    },
                    type:'post',
                    dateType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#editModal").modal("hide");
                            selectSubjectsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#editModal").modal("show");
                        }
                    }
                })
            });


            //用户进行批量选择科目进行删除
            $("#deleteSubjectBtn").click(function () {
                var str = $("#tbody input[type='checkbox']:checked");
                if(str.size() == 0){
                    alert("请先选择具体的科目, 再进行删除!!!");
                    return;
                }
                if(window.confirm("已选中" + str.size() + "条数据, 确定删除吗?")){
                    var ids = "";
                    $.each(str, function (index, object) {
                        ids += "id=" + this.value + "&";
                    });
                    ids = ids.substr(0, ids.length-1);
                    $.ajax({
                        url:"front/subject/deleteSubjectByIds.do",
                        data:ids,
                        type:'post',
                        dataType:'json',
                        success:function (data) {
                            if(data.code == "1"){
                                alert(data.message);
                                selectSubjectsByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                            }else {
                                alert(data.message);
                            }
                        }
                    });
                }

            });


            //下载所有科目信息的xls文件
            $("#exportAllSubjectBtn").click(function () {
                window.location.href="front/subject/downloadAllSubjects.do";
            });

            //显示所有
            $("#showAllSubjects").click(function () {
                $("#name").val("");
                selectSubjectsByConditionForPage(1, 10);
            });

            //页面初始化操作，加载数据页
            selectSubjectsByConditionForPage(1, 10);
        });
        //

        //通过条件检索科目
        function selectSubjectsByConditionForPage(beginNo, pageSize) {
            var name = $("#name").val();

            var beginNo = beginNo;
            var pageSize = pageSize;


            $.ajax({
                url:"front/subject/queryAllSubjectsByCondition.do",
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
                        strhtml += "<td>"+ object.name +"</td>";
                        strhtml += "<td>"+ object.information +"</td>";
                        strhtml += "<td>"+ object.score +"</td>";
                        strhtml += "<td>"+object.createTime+"</td>";
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
                            selectSubjectsByConditionForPage(pageObj.currentPage, pageObj.rowsPerPage);
                        }
                    })

                }
            })
        }

    </script>
</head>
<body>

<!-- 创建科目信息的模态窗口 -->
<div class="modal fade" id="addModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel1">创建科目信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form" id="addSubjectForm">

                    <div class="form-group">
                        <label for="add_subject_name" class="col-sm-2 control-label">名称<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="add_subject_name" class="form-control">
                        </div>
                        <label for="add_subject_score" class="col-sm-2 control-label">学分<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="add_subject_score">
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="add_subject_information" class="col-sm-2 control-label">描述</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <textarea id="add_subject_information"  class="form-control"></textarea>
                        </div>
                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveAddSubjectBtn">保存</button>
            </div>
        </div>
    </div>
</div>

<!-- 修改科目信息的模态窗口 -->
<div class="modal fade" id="editModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel2">修改科目信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form">
                    <input type="hidden" id="edit_id">
                    <div class="form-group">
                        <label for="edit_subject_name" class="col-sm-2 control-label">名称<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="edit_subject_name" class="form-control">
                        </div>
                        <label for="edit_subject_score" class="col-sm-2 control-label">学分<span style="font-size: 15px; color: red;">*</span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" class="form-control" id="edit_subject_score">
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="edit_subject_information" class="col-sm-2 control-label">描述</label>
                        <div class="col-sm-10" style="width: 300px;">

                            <textarea id="edit_subject_information"  class="form-control"></textarea>
                        </div>
                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveEditSubjectBtn">更新</button>
            </div>
        </div>
    </div>
</div>



<div>
    <div style="position: relative; left: 10px; top: -10px;">
        <div class="page-header">
            <h3>科目信息列表</h3>
        </div>
    </div>
</div>
<div style="position: relative; top: -20px; left: 0px; width: 100%; height: 100%;">
    <div style="width: 100%; position: absolute;top: 5px; left: 10px;">

        <div class="btn-toolbar" role="toolbar" style="height: 80px;">
            <form class="form-inline" role="form" style="position: relative;top: 8%; left: 5px;">

                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-addon">科目名称</div>
                        <input class="form-control" type="text" id="name">
                    </div>
                </div>

                <button type="button" class="btn btn-default" id="selectSubjectsByConditionForPageBtn">查询</button>

            </form>
        </div>
        <div class="btn-toolbar" role="toolbar" style="background-color: #F7F7F7; height: 50px; position: relative;top: 5px;">
            <div class="btn-group" style="position: relative; top: 18%;">
                <button type="button" class="btn btn-primary" id="addSubjectBtn"><span class="glyphicon glyphicon-plus"></span> 创建</button>
                <button type="button" class="btn btn-default" id="editSubjectBtn"><span class="glyphicon glyphicon-pencil"></span> 修改</button>
                <button type="button" class="btn btn-danger"  id="deleteSubjectBtn"><span class="glyphicon glyphicon-minus"></span> 删除</button>
            </div>
            <div class="btn-group" style="position: relative; top: 18%;">
                <button id="showAllSubjects" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span> 显示所有 </button>
                <button id="exportAllSubjectBtn" type="button" class="btn btn-default"><span class="glyphicon glyphicon-export"></span> 下载列表数据（批量导出）</button>

            </div>
        </div>
        <div style="position: relative;top: 10px;">
            <table class="table table-hover">
                <thead>
                <tr style="color: #B3B3B3;">
                    <td><input type="checkbox" id="checkedAll"/></td>
                    <td>名称</td>
                    <td>具体信息</td>
                    <td>学分</td>
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