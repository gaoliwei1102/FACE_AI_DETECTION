package com.gaoliwei.aaos.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class IndexController {

    @RequestMapping("/front/index/gotoIndex.do")
    public String gotoIndex(){
        return "front/index";
    }
}
