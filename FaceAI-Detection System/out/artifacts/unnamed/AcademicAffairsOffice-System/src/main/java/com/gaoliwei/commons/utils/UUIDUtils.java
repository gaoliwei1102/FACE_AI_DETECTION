package com.gaoliwei.commons.utils;

import java.util.UUID;

public class UUIDUtils {

    public static String formateId(){

        return UUID.randomUUID().toString().replaceAll("-", "");
    }

}
