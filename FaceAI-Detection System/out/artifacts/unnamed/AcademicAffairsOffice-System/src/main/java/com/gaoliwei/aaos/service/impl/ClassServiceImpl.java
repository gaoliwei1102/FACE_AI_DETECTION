package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Class;
import com.gaoliwei.aaos.mapper.ClassMapper;
import com.gaoliwei.aaos.service.ClassService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service("classService")
public class ClassServiceImpl implements ClassService {

    @Autowired
    private ClassMapper classMapper;


    @Override
    public List<Class> queryAllClassesByCondition(Map<String, Object> map) {
        return classMapper.selectAllClassesByCondition(map);
    }

    @Override
    public int addClass(Class class01) {
        return classMapper.insertClass(class01);
    }

    @Override
    public Class queryClassById(String id) {
        return classMapper.selectClassById(id);
    }

    @Override
    public int editClass(Class class01) {
        return classMapper.updateClass(class01);
    }

    @Override
    public int deleteClassByIds(String[] id) {
        return classMapper.deleteClassByIds(id);
    }

    @Override
    public List<Class> queryAllClasses() {
        return classMapper.selectAllClasses();
    }

    @Override
    public List<Class> queryAllClassByIds(String[] id) {
        return null;
    }
}
