package com.gaoliwei.aaos.controller;


import com.gaoliwei.aaos.domain.Admins;
import com.gaoliwei.aaos.service.AdminsService;
import com.gaoliwei.commons.constants.Constants;
import com.gaoliwei.commons.domain.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpSession;
import java.util.HashMap;
import java.util.Map;

@Controller
public class LoginController {

    @Autowired
    private AdminsService adminsService;


    @RequestMapping("/front/login/gotoLoginIndex.do")
    public String gotoLoginIndex(){
        return "front/login";
    }


    @RequestMapping("/front/login/MatchAdmins.do")
    public @ResponseBody Object MatchAdmins(String username, String password, HttpSession session){
        Map<String,Object> map = new HashMap<String,Object>();
        map.put("username", username);
        map.put("password", password);

        Admins admins = adminsService.queryAdminsByUsernameAndPassword(map);

        Result result = new Result();
        if (admins != null){
            session.setAttribute(Constants.SESSION_ADMINS, admins);
            result.setCode(Constants.SUCCESS_CODE);
            result.setMessage(Constants.SUCCESS_MESSAGE);
        }else {
            result.setCode(Constants.FAIL_CODE);
            result.setMessage(Constants.FAIL_MESSAGE);
        }

        return result;

    }
}
