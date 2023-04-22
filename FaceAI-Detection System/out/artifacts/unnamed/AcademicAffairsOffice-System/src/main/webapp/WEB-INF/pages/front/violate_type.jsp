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

            //点击搜索按钮按照指定条件进行搜索违规类型列表
            $("#selectViolateTypesByConditionForPageBtn").click(function () {
                selectViolateTypesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
            });

            //用户点击全选按钮时，进行所有违规类型的全选或全不选
            $("#checkedAll").click(function () {
                $("#tbody input[type='checkbox']").prop("checked", this.checked);
            });

            //当违规类型点击单个违规类型选择时，若已全部选择，激活全选按钮，否则不激活
            $("#tbody").on("click", "input[type='checkbox']", function () {
                if($("#tbody input[type='checkbox']").size() == $("#tbody input[type='checkbox']:checked").size()){
                    $("#checkedAll").prop("checked",true);
                }else {
                    $("#checkedAll").prop("checked",false);
                }
            });

            //点击创建按钮的窗口弹出操作
            $("#addViolateTypeBtn").click(function () {
                //等待进行初始化操作
                $("#addViolateTypeForm").get(0).reset();
                $("#addModal").modal("show");
            });

            //点击保存按钮需要进行的操作
            $("#saveAddViolateTypeBtn").click(function () {

                var name = $("#add_violateType_name").val();
                var grade = $("#add_violateType_grade").val();
                var info = $("#add_violateType_info").val();

                if(name == ""){
                    alert("请输入违规类型的名称!!!");
                    return;
                }
                if(grade == ""){
                    alert("请输入违规类型的等级!!!");
                    return;
                }

                if(info == ""){
                    alert("请输入违规类型的详情!!!");
                    return;
                }

                $.ajax({
                    url:"front/violateType/addViolateType.do",
                    data:{
                        name:name,
                        grade:grade,
                        info:info
                    },
                    type:'post',
                    dataType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#addModal").modal("hide");
                            selectViolateTypesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#addModal").modal("show");
                        }
                    }
                })
            });

            //打开更改违规类型信息的模态窗口
            $("#editViolateTypeBtn").click(function () {
                var editIds = $("tbody input[type='checkbox']:checked");
                if(editIds.size() == 0){
                    alert("请选择具体的一个违规类型后，再进行修改操作!!!");
                    return;
                }
                if(editIds.size() > 1){
                    alert("最多只能选择一个违规类型，才能进行修改!!!");
                    return;
                }

                var id = editIds[0].value;
                $.ajax({
                    url:'front/violateType/queryViolateTypeById.do',
                    data:{
                        id:id
                    },
                    type:'post',
                    dataType:'json',

                    success:function (data) {
                        $("#edit_id").val(data.id);
                        $("#edit_violateType_name").val(data.name);
                        $("#edit_violateType_grade").val(data.grade);
                        $("#edit_violateType_info").val(data.info);

                        $("#editModal").modal("show");

                    }
                });

            });

            //保存更改的违规类型信息
            $("#saveEditViolateTypeBtn").click(function () {

                var id = $("#edit_id").val();
                var name = $("#edit_violateType_name").val();
                var grade = $("#edit_violateType_grade").val();
                var info = $("#edit_violateType_info").val();


                if(name == ""){
                    alert("请输入违规类型的名称!!!");
                    return;
                }
                if(grade == ""){
                    alert("请输入违规类型的等级!!!");
                    return;
                }

                if(info == ""){
                    alert("请输入违规类型的详情!!!");
                    return;
                }



                $.ajax({
                    url:'front/violateType/editViolateType.do',
                    data:{
                        id:id,
                        name:name,
                        grade:grade,
                        info:info,
                    },
                    type:'post',
                    dateType:'json',
                    success:function (data) {
                        if(data.code=="1"){
                            alert(data.message);
                            $("#editModal").modal("hide");
                            selectViolateTypesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                        }else {
                            alert(data.message);
                            $("#editModal").modal("show");
                        }
                    }
                })
            });


            //用户进行批量选择违规类型进行删除
            $("#deleteViolateTypeBtn").click(function () {
                var str = $("#tbody input[type='checkbox']:checked");
                if(str.size() == 0){
                    alert("请先选择具体的违规类型, 再进行删除!!!");
                    return;
                }
                if(window.confirm("已选中" + str.size() + "条数据, 确定删除吗?")){
                    var ids = "";
                    $.each(str, function (index, object) {
                        ids += "id=" + this.value + "&";
                    });
                    ids = ids.substr(0, ids.length-1);
                    $.ajax({
                        url:"front/violateType/deleteViolateTypeByIds.do",
                        data:ids,
                        type:'post',
                        dataType:'json',
                        success:function (data) {
                            if(data.code == "1"){
                                alert(data.message);
                                selectViolateTypesByConditionForPage($("#pagination").bs_pagination("getOption", "currentPage"),
                                    $("#pagination").bs_pagination("getOption", "rowsPerPage"));
                            }else {
                                alert(data.message);
                            }
                        }
                    });
                }

            });


            //下载所有违规类型信息的xls文件
            $("#exportAllViolateTypeBtn").click(function () {
                window.location.href="front/violateType/downloadAllViolateTypes.do";
            });

            //显示所有
            $("#showAllViolateTypes").click(function () {
                $("#name").val("");
                selectViolateTypesByConditionForPage(1, 10);
            });

            //页面初始化操作，加载数据页
            selectViolateTypesByConditionForPage(1, 10);
        });
        //

        //通过条件检索违规类型
        function selectViolateTypesByConditionForPage(beginNo, pageSize) {
            var name = $("#name").val();

            var beginNo = beginNo;
            var pageSize = pageSize;


            $.ajax({
                url:"front/violateType/queryAllViolateTypesByCondition.do",
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
                        strhtml += "<td>"+ object.grade +"</td>";
                        strhtml += "<td>"+ object.info +"</td>";
                        strhtml += "<td>"+ object.createTime +"</td>";
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
                            selectViolateTypesByConditionForPage(pageObj.currentPage, pageObj.rowsPerPage);
                        }
                    })

                }
            })
        }

    </script>
</head>
<body>

<!-- 创建违规类型信息的模态窗口 -->
<div class="modal fade" id="addModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel1">创建违规类型信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form" id="addViolateTypeForm">

                    <div class="form-group">
                        <label for="add_violateType_name" class="col-sm-2 control-label">名称</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="add_violateType_name" class="form-control">
                        </div>
                        <label for="add_violateType_grade" class="col-sm-2 control-label">等级</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="add_violateType_grade" class="form-control">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="add_violateType_info" class="col-sm-2 control-label">详情<span style="font-size: 15px; color: red;"></span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <textarea type="text" id="add_violateType_info" class="form-control"></textarea>
                        </div>
                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveAddViolateTypeBtn">保存</button>
            </div>
        </div>
    </div>
</div>

<!-- 修改违规类型信息的模态窗口 -->
<div class="modal fade" id="editModal" role="dialog">
    <div class="modal-dialog" role="document" style="width: 85%;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title" id="myModalLabel2">修改违规类型信息</h4>
            </div>
            <div class="modal-body">

                <form class="form-horizontal" role="form">
                    <input type="hidden" id="edit_id">


                    <div class="form-group">
                        <label for="edit_violateType_name" class="col-sm-2 control-label">名称</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <input type="text" id="edit_violateType_name" class="form-control">
                        </div>
                        <label for="edit_violateType_grade" class="col-sm-2 control-label">等级</label>
                        <div class="col-sm-10" style="width: 300px;">
                            <select id="edit_violateType_grade" class="form-control">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="edit_violateType_info" class="col-sm-2 control-label">详情<span style="font-size: 15px; color: red;"></span></label>
                        <div class="col-sm-10" style="width: 300px;">
                            <textarea type="text" id="edit_violateType_info" class="form-control"></textarea>
                        </div>
                    </div>

                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary" id="saveEditViolateTypeBtn">更新</button>
            </div>
        </div>
    </div>
</div>



<div>
    <div style="position: relative; left: 10px; top: -10px;">
        <div class="page-header">
            <h3>违规类型信息列表</h3>
        </div>
    </div>
</div>
<div style="position: relative; top: -20px; left: 0px; width: 100%; height: 100%;">
    <div style="width: 100%; position: absolute;top: 5px; left: 10px;">

        <div class="btn-toolbar" role="toolbar" style="height: 80px;">
            <form class="form-inline" role="form" style="position: relative;top: 8%; left: 5px;">

                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-addon">违规类型</div>
                        <input class="form-control" type="text" id="name">
                    </div>
                </div>

                <button type="button" class="btn btn-default" id="selectViolateTypesByConditionForPageBtn">查询</button>

            </form>
        </div>
        <div class="btn-toolbar" role="toolbar" style="background-color: #F7F7F7; height: 50px; position: relative;top: 5px;">
            <div class="btn-group" style="position: relative; top: 18%;">
                <button type="button" class="btn btn-primary" id="addViolateTypeBtn"><span class="glyphicon glyphicon-plus"></span> 创建</button>
                <button type="button" class="btn btn-default" id="editViolateTypeBtn"><span class="glyphicon glyphicon-pencil"></span> 修改</button>
                <button type="button" class="btn btn-danger"  id="deleteViolateTypeBtn"><span class="glyphicon glyphicon-minus"></span> 删除</button>
            </div>
            <div class="btn-group" style="position: relative; top: 18%;">
                <button id="showAllViolateTypes" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-center"></span> 显示所有 </button>
                <button id="exportAllViolateTypeBtn" type="button" class="btn btn-default"><span class="glyphicon glyphicon-export"></span> 下载列表数据（批量导出）</button>

            </div>
        </div>
        <div style="position: relative;top: 10px;">
            <table class="table table-hover">
                <thead>
                <tr style="color: #B3B3B3;">
                    <td><input type="checkbox" id="checkedAll"/></td>
                    <td>违规名称</td>
                    <td>违规等级</td>
                    <td>违规详解</td>
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