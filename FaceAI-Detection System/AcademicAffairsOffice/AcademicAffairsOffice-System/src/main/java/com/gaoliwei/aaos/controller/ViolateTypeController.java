package com.gaoliwei.aaos.controller;

import com.gaoliwei.aaos.domain.ViolateType;
import com.gaoliwei.aaos.service.ViolateTypeService;
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
public class ViolateTypeController {

    @Autowired
    private ViolateTypeService violateTypeService;

    @RequestMapping("/front/violateType/gotoViolateTypeIndex.do")
    public String gotoViolateTypeIndex(){
        return "front/violate_type";
    }


    @RequestMapping("/front/violateType/queryAllViolateTypesByCondition.do")
    public @ResponseBody List<ViolateType> queryAllViolateTypesByCondition(String name, int beginNo, int pageSize){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("name",name);
        map.put("beginNo",(beginNo-1)*pageSize);
        map.put("pageSize",pageSize);

        List<ViolateType> violateTypes = violateTypeService.queryAllViolateTypesByCondition(map);

        return violateTypes;
    }



    @RequestMapping("/front/violateType/addViolateType.do")
    public @ResponseBody Object addViolateType(String name, Integer grade, String info){

        ViolateType violateType = new ViolateType();

        violateType.setId(UUIDUtils.formateId());
        violateType.setName(name);
        violateType.setGrade(grade);
        violateType.setInfo(info);
        violateType.setCreateTime(DateUtils.formateDateTime(new Date()));

        int ret = violateTypeService.addViolateType(violateType);

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


    @RequestMapping("/front/violateType/queryViolateTypeById.do")
    public @ResponseBody ViolateType queryViolateTypeById(String id){
        ViolateType violateType = violateTypeService.queryViolateTypeById(id);

        return violateType;
    }

    @RequestMapping("/front/violateType/editViolateType.do")
    public @ResponseBody Object editViolateType(String id, String name, Integer grade, String info){
        ViolateType violateType = new ViolateType();

        violateType.setId(id);
        violateType.setName(name);
        violateType.setGrade(grade);
        violateType.setInfo(info);
        violateType.setCreateTime(DateUtils.formateDateTime(new Date()));

        int ret = violateTypeService.editViolateType(violateType);

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

    @RequestMapping("/front/violateType/deleteViolateTypeByIds.do")
    public @ResponseBody Object deleteViolateTypeByIds(String[] id){
        int ret = violateTypeService.deleteViolateTypeByIds(id);

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

    @RequestMapping("/front/violateType/downloadAllViolateTypes.do")
    public void downloadAllViolateTypes(HttpServletResponse response) throws Exception{

        response.setContentType("application/octet-stream");
        response.setHeader("Content-Disposition","attachment;filename=ViolateTypesExcel.xls");

        List<ViolateType> violateTypes = violateTypeService.queryAllViolateTypes();

        HSSFWorkbook sheets = new HSSFWorkbook();
        HSSFSheet sheet = sheets.createSheet();
        HSSFRow row = sheet.createRow(0);
        HSSFCell cell = row.createCell(0);
        cell.setCellValue("ID");
        cell = row.createCell(1);
        cell.setCellValue("违规名称");
        cell = row.createCell(2);
        cell.setCellValue("违规等级");
        cell = row.createCell(3);
        cell.setCellValue("违规详情");
        cell = row.createCell(4);
        cell.setCellValue("创建时间");
        ViolateType violateType = null;
        if(violateTypes!=null && violateTypes.size()>0){
            for (int i=0; i<violateTypes.size(); i++){
                violateType = violateTypes.get(i);
                row = sheet.createRow(i+1);
                cell = row.createCell(0);
                cell.setCellValue(violateType.getId());
                cell = row.createCell(1);
                cell.setCellValue(violateType.getName());
                cell = row.createCell(2);
                cell.setCellValue(violateType.getGrade().toString());
                cell = row.createCell(3);
                cell.setCellValue(violateType.getInfo());
                cell = row.createCell(4);
                cell.setCellValue(violateType.getCreateTime());
            }
        }


        ServletOutputStream outputStream = response.getOutputStream();
        sheets.write(outputStream);

        sheets.close();
        outputStream.flush();
    }

}



