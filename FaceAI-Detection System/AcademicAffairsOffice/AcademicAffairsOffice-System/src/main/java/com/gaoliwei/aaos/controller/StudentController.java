package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.Class;
import com.gaoliwei.aaos.domain.Student;
import com.gaoliwei.aaos.service.ClassService;
import com.gaoliwei.aaos.service.StudentService;
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
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


@Controller
public class StudentController {

    @Autowired
    private StudentService studentService;

    @Autowired
    private ClassService classService;

    @RequestMapping("/front/student/gotoStudentIndex.do")
    public String gotoStudentIndex(HttpServletRequest request){
        List<Class> classes = classService.queryAllClasses();
        request.setAttribute("classes", classes);

        return "front/student";
    }


    @RequestMapping("/front/student/queryAllStudentsByCondition.do")
    public @ResponseBody
    List<Student> queryAllStudentsByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<Student> students = studentService.queryAllStudentsByCondition(map);

        return students;
    }



    @RequestMapping("/front/student/addStudent.do")
    public @ResponseBody Object addStudent(String student_no, String password, String name,  Integer age, String gender, String belong_class, Integer face_num){

        Student student = new Student();

        student.setId(UUIDUtils.formateId());
        student.setStudentNo(student_no);
        student.setPassword(password);
        student.setName(name);
        student.setGender(gender);
        student.setAge(age);
        student.setBelongClass(belong_class);
        student.setFaceNum(face_num);

        int ret = studentService.addStudent(student);

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


    @RequestMapping("/front/student/queryStudentById.do")
    public @ResponseBody Student queryStudentById(String id){
        Student student = studentService.queryStudentById(id);

        return student;
    }

    @RequestMapping("/front/student/editStudent.do")
    public @ResponseBody Object editStudent(String id, String student_no, String password, String name,  Integer age, String gender, String belong_class, Integer face_num){
        Student student = new Student();


        student.setId(id);
        student.setStudentNo(student_no);
        student.setPassword(password);
        student.setName(name);
        student.setGender(gender);
        student.setAge(age);
        student.setBelongClass(belong_class);
        student.setFaceNum(face_num);

        int ret = studentService.editStudent(student);

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


    @RequestMapping("/front/student/deleteStudentByIds.do")
    public @ResponseBody Object deleteStudentByIds(String[] id){
        int ret = studentService.deleteStudentByIds(id);

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

    @RequestMapping("/front/student/downloadAllStudents.do")
    public void downloadAllStudents(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=StudentsExcel.xls");

        List<Student> students = studentService.queryAllStudents();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("ID");
        cell = row.createCell(1);
        cell.setCellValue("学号");
        cell = row.createCell(2);
        cell.setCellValue("密钥");
        cell = row.createCell(3);
        cell.setCellValue("姓名");
        cell = row.createCell(4);
        cell.setCellValue("年龄");
        cell = row.createCell(5);
        cell.setCellValue("性别");
        cell = row.createCell(6);
        cell.setCellValue("所属班级");
        cell = row.createCell(7);
        cell.setCellValue("人脸数目");


        Student student = null;
        if(students!=null && students.size()>0){
            for (int i=0; i<students.size(); i++){
                student = students.get(i);
                row = sheet.createRow(i+1);
                cell = row.createCell(0);
                cell.setCellValue(student.getId());
                cell = row.createCell(1);
                cell.setCellValue(student.getStudentNo());
                cell = row.createCell(2);
                cell.setCellValue(student.getPassword());
                cell = row.createCell(3);
                cell.setCellValue(student.getName());
                cell = row.createCell(4);
                cell.setCellValue(student.getAge().toString());
                cell = row.createCell(5);
                cell.setCellValue(student.getGender());
                cell = row.createCell(6);
                cell.setCellValue(student.getBelongClass());
                cell = row.createCell(7);
                cell.setCellValue(student.getFaceNum().toString());
            }
        }


        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }

}
