package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Teacher;
import com.gaoliwei.aaos.mapper.TeacherMapper;
import com.gaoliwei.aaos.service.TeacherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service("teacherService")
public class TeacherServiceImpl implements TeacherService {

    @Autowired
    private TeacherMapper teacherMapper;


    @Override
    public List<Teacher> queryAllTeachersByCondition(Map<String, Object> map) {

        return teacherMapper.selectAllTeachersByCondition(map);
    }

    @Override
    public int addTeacher(Teacher teacher) {
        return teacherMapper.insertTeacher(teacher);
    }

    @Override
    public Teacher queryTeacherById(String id) {
        return teacherMapper.selectTeacherById(id);
    }

    @Override
    public int editTeacher(Teacher teacher) {
        return teacherMapper.updateTeacher(teacher);
    }

    @Override
    public int deleteTeacherByIds(String[] id) {
        return teacherMapper.deleteTeacherByIds(id);
    }

    @Override
    public List<Teacher> queryAllTeachers() {
        return teacherMapper.selectAllTeachers();
    }

    @Override
    public List<Teacher> queryAllTeacherByIds(String[] id) {
        return teacherMapper.selectAllTeacherByIds(id);
    }
}
