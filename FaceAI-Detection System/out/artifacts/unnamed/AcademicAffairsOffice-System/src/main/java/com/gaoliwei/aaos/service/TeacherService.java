package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Teacher;
import org.apache.poi.ss.formula.functions.T;

import java.util.List;
import java.util.Map;

public interface TeacherService {


    public List<Teacher> queryAllTeachersByCondition(Map<String,Object> map);


    int addTeacher(Teacher teacher);

    Teacher queryTeacherById(String id);

    int editTeacher(Teacher teacher);

    int deleteTeacherByIds(String[] id);

    List<Teacher> queryAllTeachers();

    List<Teacher> queryAllTeacherByIds(String[] id);
}
