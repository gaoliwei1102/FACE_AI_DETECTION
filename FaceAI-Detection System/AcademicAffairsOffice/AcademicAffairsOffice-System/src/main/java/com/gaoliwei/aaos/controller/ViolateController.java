package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.*;
import com.gaoliwei.aaos.domain.Class;
import com.gaoliwei.aaos.service.*;
import com.gaoliwei.commons.constants.Constants;
import com.gaoliwei.commons.domain.Result;
import com.gaoliwei.commons.utils.DateUtils;
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
import java.util.*;

@Controller
public class ViolateController {

    @Autowired
    private ViolateService violateService;

    @Autowired
    private  CourseService courseService;

    @Autowired
    private StudentService studentService;

    @Autowired
    private ViolateTypeService violateTypeService;

    @Autowired
    private TeacherService teacherService;

    @Autowired
    private SubjectService subjectService;

    @Autowired ClassService classService;

    @RequestMapping("/front/violate/gotoViolateIndex.do")
    public String gotoViolateIndex(HttpServletRequest request){
        List<ViolateType> violateTypes = violateTypeService.queryAllViolateTypes();

        request.setAttribute("violateTypes",violateTypes);


        return "front/violate";
    }


    @RequestMapping("/front/violate/queryAllViolatesByCondition.do")
    public @ResponseBody Map<String, Object> queryAllViolatesByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<Violate> violates = violateService.queryAllViolatesByCondition(map);
        List<Course> courses = new ArrayList<Course>();
        List<Teacher> teachers = new ArrayList<Teacher>();
        List<Subject> subjects = new ArrayList<Subject>();
        List<Class> classes = new ArrayList<Class>();

        for (int i = 0; i < violates.size(); i++){
            String course_id = violates.get(i).getCourse();
            Course course = courseService.queryCourseById(course_id);
            Teacher teacher = teacherService.queryTeacherById(course.getTeacher());
            Subject subject = subjectService.querySubjectById(course.getSubject());
            Class clas = classService.queryClassById(course.getTblClass());
            courses.add(course);
            teachers.add(teacher);
            subjects.add(subject);
            classes.add(clas);

        }

        Map<String, Object> resultMap = new HashMap<String, Object>();
        resultMap.put("violates", violates);
        resultMap.put("courses", courses);
        resultMap.put("teachers", teachers);
        resultMap.put("subjects", subjects);
        resultMap.put("classes", classes);

        return resultMap;
    }


    @RequestMapping("/front/violate/addViolate.do")
    public @ResponseBody Object addViolate(String type, String course, String student, String remarks){

        Violate violate = new Violate();

        violate.setId(UUIDUtils.formateId());
        violate.setType(type);
        violate.setCourse(course);
        violate.setStudent(student);
        violate.setRemarks(remarks);
        violate.setCreateTime(DateUtils.formateDateTime(new Date()));

        int ret = violateService.addViolate(violate);

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


    @RequestMapping("/front/violate/queryViolateById.do")
    public @ResponseBody Map<String, Object> queryViolateById(String id){
        Violate violate = violateService.queryViolateById(id);

        String tblClass = courseService.queryCourseById(violate.getCourse()).getTblClass();

        List<Student> students = studentService.queryAllStudents();
        List<Student> belong_students = new ArrayList<Student>();


        for (int i =  0; i < students.size(); i++){
            if (students.get(i).getBelongClass().equals(tblClass)){
                belong_students.add(students.get(i));
            }
        }

        Map<String, Object> map = new HashMap<String, Object>();

        map.put("violate",violate);
        map.put("students", belong_students);

        return map;
    }


    @RequestMapping("/front/violate/editViolate.do")
    public @ResponseBody Object editViolate(String id, String course, String type, String student, String remarks) {
        Violate violate = new Violate();

        violate.setId(id);
        violate.setCourse(course);
        violate.setType(type);
        violate.setStudent(student);
        violate.setRemarks(remarks);

        int ret = violateService.editViolate(violate);

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


    @RequestMapping("/front/violate/deleteViolateByIds.do")
    public @ResponseBody Object deleteViolateByIds(String[] id){
        int ret = violateService.deleteViolateByIds(id);

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


    @RequestMapping("/front/violate/downloadAllViolates.do")
    public void downloadAllViolates(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=ViolatesExcel.xls");

        List<Violate> violates = violateService.queryAllViolates();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("违规ID");
        cell = row.createCell(1);
        cell.setCellValue("违规名称");
        cell = row.createCell(2);
        cell.setCellValue("学生姓名");
        cell = row.createCell(3);
        cell.setCellValue("所属班级");
        cell = row.createCell(4);
        cell.setCellValue("课程名称");
        cell = row.createCell(5);
        cell.setCellValue("授课老师");
        cell = row.createCell(6);
        cell.setCellValue("课程日期");
        cell = row.createCell(7);
        cell.setCellValue("开始时间");
        cell = row.createCell(8);
        cell.setCellValue("结束时间");
        cell = row.createCell(9);
        cell.setCellValue("备注");
        cell = row.createCell(10);
        cell.setCellValue("创建时间");

        List<Course> courses = new ArrayList<Course>();
        List<Teacher> teachers = new ArrayList<Teacher>();
        List<Subject> subjects = new ArrayList<Subject>();
        List<Class> classes = new ArrayList<Class>();
        List<ViolateType> violateTypes = new ArrayList<ViolateType>();

        for (int i = 0; i < violates.size(); i++){
            String course_id = violates.get(i).getCourse();
            Course course = courseService.queryCourseById(course_id);
            Teacher teacher = teacherService.queryTeacherById(course.getTeacher());
            Subject subject = subjectService.querySubjectById(course.getSubject());
            Class clas = classService.queryClassById(course.getTblClass());
            ViolateType violateType = violateTypeService.queryViolateTypeById(violates.get(i).getType());
            courses.add(course);
            teachers.add(teacher);
            subjects.add(subject);
            classes.add(clas);
            violateTypes.add(violateType);
        }

        Violate violate = new Violate();
        if(violates!=null && violates.size()>0){
            for (int i=0; i<violates.size(); i++){
                Student student = new Student();
                violate = violates.get(i);
                row = sheet.createRow(i+1);
                cell = row.createCell(0);
                cell.setCellValue(violate.getId());
                cell = row.createCell(1);
                cell.setCellValue(violateTypes.get(i).getName());
                cell = row.createCell(2);
                cell.setCellValue(studentService.queryStudentById(violate.getStudent()).getName());
                cell = row.createCell(3);
                cell.setCellValue(classes.get(i).getName());
                cell = row.createCell(4);
                cell.setCellValue(subjects.get(i).getName());
                cell = row.createCell(5);
                cell.setCellValue(teachers.get(i).getName());
                cell = row.createCell(6);
                cell.setCellValue(courses.get(i).getStartDay());
                cell = row.createCell(7);
                cell.setCellValue(courses.get(i).getStartTime());
                cell = row.createCell(8);
                cell.setCellValue(courses.get(i).getEndTime());
                cell = row.createCell(9);
                cell.setCellValue(violate.getRemarks());
                cell = row.createCell(10);
                cell.setCellValue(violate.getCreateTime());
            }
        }


        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }

}



