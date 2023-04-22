package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Class;

import java.util.List;
import java.util.Map;

public interface ClassService {

    public List<Class> queryAllClassesByCondition(Map<String,Object> map);


    int addClass(Class class01);

    Class queryClassById(String id);

    int editClass(Class class01);

    int deleteClassByIds(String[] id);

    List<Class> queryAllClasses();

    List<Class> queryAllClassByIds(String[] id);
}
