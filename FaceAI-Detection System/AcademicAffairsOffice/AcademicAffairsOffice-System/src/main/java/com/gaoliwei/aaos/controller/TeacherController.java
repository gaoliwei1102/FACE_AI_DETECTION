package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.Teacher;
import com.gaoliwei.aaos.service.TeacherService;
import com.gaoliwei.commons.constants.Constants;
import com.gaoliwei.commons.domain.Result;
import com.gaoliwei.commons.utils.UUIDUtils;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class TeacherController {

    @Autowired
    private TeacherService teacherService;

    @RequestMapping("/front/teacher/gotoTeacherIndex.do")
    public String gotoTeacherIndex(){
        return "front/teacher";
    }


    @RequestMapping("/front/teacher/queryAllTeachersByCondition.do")
    public @ResponseBody List<Teacher> queryAllTeachersByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<Teacher> teachers = teacherService.queryAllTeachersByCondition(map);

        return teachers;
    }



    @RequestMapping("/front/teacher/addTeacher.do")
    public @ResponseBody Object addTeacher(String teacher_no, String password, String name, Integer age, String gender, String phone, String email){

        Teacher teacher = new Teacher();

        teacher.setId(UUIDUtils.formateId());
        teacher.setTeacherNo(teacher_no);
        teacher.setPassword(password);
        teacher.setName(name);
        teacher.setAge(age);
        teacher.setGender(gender);
        teacher.setPhone(phone);
        teacher.setEmail(email);

        int ret = teacherService.addTeacher(teacher);

        Result result = new Result();
        if (ret > 0){
            result.setCode(Constants.SUCCESS_CODE);
            result.setMessage(Constants.SUCCESS_MESSAGE);
        }else {
            result.setCode(Constants.FAIL_CODE);
            result.setMessage(Constants.FAIL_MESSAGE);
        }

        return result;
    }


    @RequestMapping("/front/teacher/queryTeacherById.do")
    public @ResponseBody Teacher queryTeacherById(String id){
        Teacher teacher = teacherService.queryTeacherById(id);

        return teacher;
    }

    @RequestMapping("/front/teacher/editTeacher.do")
    public @ResponseBody Object editTeacher(String teacher_no, String password, String id, String name, Integer age, String gender, String phone, String email){
        Teacher teacher = new Teacher();

        teacher.setId(id);
        teacher.setTeacherNo(teacher_no);
        teacher.setPassword(password);
        teacher.setName(name);
        teacher.setAge(age);
        teacher.setGender(gender);
        teacher.setPhone(phone);
        teacher.setEmail(email);

        int ret = teacherService.editTeacher(teacher);

        Result result = new Result();
        if (ret > 0){
            result.setCode(Constants.SUCCESS_CODE);
            result.setMessage(Constants.SUCCESS_MESSAGE);
        }else {
            result.setCode(Constants.FAIL_CODE);
            result.setMessage(Constants.FAIL_MESSAGE);
        }

        return result;
    }

    @RequestMapping("/front/teacher/deleteTeacherByIds.do")
    public @ResponseBody Object deleteTeacherByIds(String[] id){
        int ret = teacherService.deleteTeacherByIds(id);

        Result result = new Result();
        if (ret == id.length){
            result.setCode(Constants.SUCCESS_CODE);
            result.setMessage(Constants.SUCCESS_MESSAGE);
        }else {
            result.setCode(Constants.FAIL_CODE);
            result.setMessage(Constants.FAIL_MESSAGE);
        }

        return result;
    }

    @RequestMapping("/front/teacher/downloadAllTeachers.do")
    public void downloadAllTeachers(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=TeachersExcel.xls");

        List<Teacher> teachers = teacherService.queryAllTeachers();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("ID");
        cell = row.createCell(1);
        cell.setCellValue("编号");
        cell = row.createCell(2);
        cell.setCellValue("密钥");
        cell = row.createCell(3);
        cell.setCellValue("姓名");
        cell = row.createCell(4);
        cell.setCellValue("年龄");
        cell = row.createCell(5);
        cell.setCellValue("性别");
        cell = row.createCell(6);
        cell.setCellValue("电话");
        cell = row.createCell(7);
        cell.setCellValue("Email");

        Teacher teacher = null;
        if(teachers!=null && teachers.size()>0){
            for (int i=0; i<teachers.size(); i++){
                teacher = teachers.get(i);
                row = sheet.createRow(i+1);
                cell = row.createCell(0);
                cell.setCellValue(teacher.getId());
                cell = row.createCell(1);
                cell.setCellValue(teacher.getTeacherNo());
                cell = row.createCell(2);
                cell.setCellValue(teacher.getPassword());
                cell = row.createCell(3);
                cell.setCellValue(teacher.getName());
                cell = row.createCell(4);
                cell.setCellValue(teacher.getAge().toString());
                cell = row.createCell(5);
                cell.setCellValue(teacher.getGender());
                cell = row.createCell(6);
                cell.setCellValue(teacher.getPhone());
                cell = row.createCell(7);
                cell.setCellValue(teacher.getEmail());
            }
        }


        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }

}



