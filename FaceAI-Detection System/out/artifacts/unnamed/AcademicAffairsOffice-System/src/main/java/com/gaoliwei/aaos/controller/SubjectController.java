package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.Subject;
import com.gaoliwei.aaos.service.SubjectService;
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
import javax.servlet.http.HttpServletResponse;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class SubjectController {

    @Autowired
    private SubjectService subjectService;

    @RequestMapping("/front/subject/gotoSubjectIndex.do")
    public String gotoSubjectIndex(){
        return "front/subject";
    }


    @RequestMapping("/front/subject/queryAllSubjectsByCondition.do")
    public @ResponseBody
    List<Subject> queryAllSubjectsByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<Subject> subjects = subjectService.queryAllSubjectsByCondition(map);

        return subjects;
    }



    @RequestMapping("/front/subject/addSubject.do")
    public @ResponseBody Object addSubject(String name, String information, Float score){

        Subject subject = new Subject();

        subject.setId(UUIDUtils.formateId());
        subject.setName(name);
        subject.setInformation(information);
        subject.setScore(score);
        subject.setCreateTime(DateUtils.formateDateTime(new Date()));

        int ret = subjectService.addSubject(subject);

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


    @RequestMapping("/front/subject/querySubjectById.do")
    public @ResponseBody Subject querySubjectById(String id){
        Subject subject = subjectService.querySubjectById(id);

        return subject;
    }


    @RequestMapping("/front/subject/editSubject.do")
    public @ResponseBody Object editSubject(String id, String name, String information, Float score){
        Subject subject = new Subject();

        subject.setId(id);
        subject.setName(name);
        subject.setInformation(information);
        subject.setScore(score);

        int ret = subjectService.editSubject(subject);

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

    @RequestMapping("/front/subject/deleteSubjectByIds.do")
    public @ResponseBody Object deleteSubjectByIds(String[] id){
        int ret = subjectService.deleteSubjectByIds(id);

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

    @RequestMapping("/front/subject/downloadAllSubjects.do")
    public void downloadAllSubjects(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=SubjectsExcel.xls");

        List<Subject> subjects = subjectService.queryAllSubjects();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("ID");
        cell = row.createCell(1);
        cell.setCellValue("科目名称");
        cell = row.createCell(2);
        cell.setCellValue("科目学分");
        cell = row.createCell(3);
        cell.setCellValue("简介");
        cell = row.createCell(4);
        cell.setCellValue("创建时间");

        Subject subject = null;
        if(subjects!=null && subjects.size()>0){
            for (int i=0; i<subjects.size(); i++){
                subject = subjects.get(i);
                row = sheet.createRow(i+1);
                cell = row.createCell(0);
                cell.setCellValue(subject.getId());
                cell = row.createCell(1);
                cell.setCellValue(subject.getName());
                cell = row.createCell(2);
                cell.setCellValue(subject.getInformation());
                cell = row.createCell(3);
                cell.setCellValue(subject.getScore().toString());
                cell = row.createCell(4);
                cell.setCellValue(subject.getCreateTime());
            }
        }


        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }
    
}
