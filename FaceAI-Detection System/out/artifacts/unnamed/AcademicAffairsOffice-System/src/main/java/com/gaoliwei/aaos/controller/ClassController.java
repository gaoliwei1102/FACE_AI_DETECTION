package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.Class;
import com.gaoliwei.aaos.service.ClassService;
import com.gaoliwei.commons.constants.Constants;
import com.gaoliwei.commons.domain.Result;
import com.gaoliwei.commons.utils.UUIDUtils;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class ClassController {

    @Autowired
    private ClassService classService;

    @RequestMapping("/front/class/gotoClassIndex.do")
    public String gotoClassIndex(){
        return "front/class";
    }


    @RequestMapping("/front/class/queryAllClassesByCondition.do")
    public @ResponseBody
    List<Class> queryAllClassesByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<Class> classes = classService.queryAllClassesByCondition(map);

        return classes;
    }



    @RequestMapping("/front/class/addClass.do")
    public @ResponseBody Object addClass(String name, Integer mumber){

        Class class01 = new Class();

        class01.setId(UUIDUtils.formateId());
        class01.setName(name);
        class01.setMumber(mumber);

        int ret = classService.addClass(class01);

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


    @RequestMapping("/front/class/queryClassById.do")
    public @ResponseBody Class queryClassById(String id){
        Class class01 = classService.queryClassById(id);

        return class01;
    }

    @RequestMapping("/front/class/editClass.do")
    public @ResponseBody Object editClass(String id, String name, Integer mumber){
        Class class01 = new Class();

        class01.setId(id);
        class01.setName(name);
        class01.setMumber(mumber);

        int ret = classService.editClass(class01);

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

    @RequestMapping("/front/class/deleteClassByIds.do")
    public @ResponseBody Object deleteClassByIds(String[] id){
        int ret = classService.deleteClassByIds(id);

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

    @RequestMapping("/front/class/downloadAllClasses.do")
    public void downloadAllClasses(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=ClassesExcel.xls");

        List<Class> classes = classService.queryAllClasses();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("ID");
        cell = row.createCell(1);
        cell.setCellValue("名称");
        cell = row.createCell(2);
        cell.setCellValue("班级");

        Class clas = null;

        if (classes!=null && classes.size()>0) {

            for (int i = 0; i < classes.size(); i++) {
                clas = classes.get(i);
                row = sheet.createRow(i + 1);
                cell = row.createCell(0);
                cell.setCellValue(clas.getId());
                cell = row.createCell(1);
                cell.setCellValue(clas.getName());
                cell = row.createCell(2);
                cell.setCellValue(clas.getMumber().toString());

            }
        }

        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }
}
