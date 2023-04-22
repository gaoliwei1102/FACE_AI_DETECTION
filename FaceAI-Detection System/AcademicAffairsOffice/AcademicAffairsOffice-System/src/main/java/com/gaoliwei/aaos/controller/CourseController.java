package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.Class;
import com.gaoliwei.aaos.domain.Course;
import com.gaoliwei.aaos.domain.Subject;
import com.gaoliwei.aaos.domain.Teacher;
import com.gaoliwei.aaos.service.ClassService;
import com.gaoliwei.aaos.service.CourseService;
import com.gaoliwei.aaos.service.SubjectService;
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
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class CourseController {

    @Autowired
    private ClassService classService;
    @Autowired
    private SubjectService subjectService;
    @Autowired
    private TeacherService teacherService;
    @Autowired
    private CourseService courseService;


    @RequestMapping("/front/course/gotoCourseIndex.do")
    public String gotoCourseIndex(HttpServletRequest request){
        List<Subject> subjects = subjectService.queryAllSubjects();
        List<Class> classes = classService.queryAllClasses();
        List<Teacher> teachers = teacherService.queryAllTeachers();

        request.setAttribute("subjects", subjects);
        request.setAttribute("classes", classes);
        request.setAttribute("teachers", teachers);

        return "front/course";
    }


    @RequestMapping("/front/course/queryAllCoursesByCondition.do")
    public @ResponseBody
    List<Course> queryAllCoursesByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<Course> courses = courseService.queryAllCoursesByCondition(map);

        return courses;
    }



    @RequestMapping("/front/course/addCourse.do")
    public @ResponseBody Object addCourse(String subject, String teacher, String tbl_class, String start_day, String start_time, String end_time, String remarks){

        Course course = new Course();

        course.setId(UUIDUtils.formateId());
        course.setSubject(subject);
        course.setTeacher(teacher);
        course.setTblClass(tbl_class);
        course.setStartDay(start_day);
        course.setStartTime(start_time);
        course.setEndTime(end_time);
        course.setRemarks(remarks);

        int ret = courseService.addCourse(course);

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


    @RequestMapping("/front/course/queryCourseById.do")
    public @ResponseBody Course queryCourseById(String id){
        Course course = courseService.queryCourseById(id);


        return course;
    }


    @RequestMapping("/front/course/editCourse.do")
    public @ResponseBody Object editCourse(String id, String subject, String teacher, String tbl_class, String start_day, String start_time, String end_time, String remarks){
        Course course = new Course();


        course.setId(id);
        course.setSubject(subject);
        course.setTeacher(teacher);
        course.setTblClass(tbl_class);
        course.setStartDay(start_day);
        course.setStartTime(start_time);
        course.setEndTime(end_time);
        course.setRemarks(remarks);

        int ret = courseService.editCourse(course);

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


    @RequestMapping("/front/course/deleteCourseByIds.do")
    public @ResponseBody Object deleteCourseByIds(String[] id){
        int ret = courseService.deleteCourseByIds(id);

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

    @RequestMapping("/front/course/downloadAllCourses.do")
    public void downloadAllCourses(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=CoursesExcel.xls");

        List<Course> courses = courseService.queryAllCourses();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("ID");
        cell = row.createCell(1);
        cell.setCellValue("科目");
        cell = row.createCell(2);
        cell.setCellValue("教师");
        cell = row.createCell(3);
        cell.setCellValue("班级");
        cell = row.createCell(4);
        cell.setCellValue("开始日期");
        cell = row.createCell(5);
        cell.setCellValue("开始时间");
        cell = row.createCell(6);
        cell.setCellValue("结束时间");
        cell = row.createCell(7);
        cell.setCellValue("备注");


        Course course = null;
        if(courses!=null && courses.size()>0){
            for (int i=0; i<courses.size(); i++){
                course = courses.get(i);
                row = sheet.createRow(i+1);
                cell = row.createCell(0);
                cell.setCellValue(course.getId());
                cell = row.createCell(1);
                cell.setCellValue(course.getSubject());
                cell = row.createCell(2);
                cell.setCellValue(course.getTeacher());
                cell = row.createCell(3);
                cell.setCellValue(course.getTblClass());
                cell = row.createCell(4);
                cell.setCellValue(course.getStartDay());
                cell = row.createCell(5);
                cell.setCellValue(course.getStartTime());
                cell = row.createCell(6);
                cell.setCellValue(course.getEndTime());
                cell = row.createCell(7);
                cell.setCellValue(course.getRemarks());
            }
        }


        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }
    
    
    
}
