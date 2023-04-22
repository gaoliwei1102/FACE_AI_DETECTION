package com.gaoliwei.aaos.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class InfoController {

    @RequestMapping("/front/info/gotoInfoIndex.do")
    public String gotoInfoIndex(){
        return "front/info";
    }
}
