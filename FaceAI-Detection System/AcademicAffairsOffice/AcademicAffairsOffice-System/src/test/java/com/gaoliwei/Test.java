package com.gaoliwei;

import com.gaoliwei.commons.utils.DateUtils;

import java.util.Date;
import java.util.UUID;

;

public class Test {

    public static void main(String[] args) throws Exception {

        System.out.println(UUID.randomUUID().toString().replaceAll("-",""));
        System.out.println(DateUtils.formateDateTime(new Date()));

    }

}
