package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Course;
import com.gaoliwei.aaos.mapper.CourseMapper;
import com.gaoliwei.aaos.service.CourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service("courseService")
public class CourseServiceImpl implements CourseService {

    @Autowired
    private CourseMapper courseMapper;


    @Override
    public List<Course> queryAllCoursesByCondition(Map<String, Object> map) {
        return courseMapper.selectAllCoursesByCondition(map);
    }

    @Override
    public int addCourse(Course course) {
        return courseMapper.insertCourse(course);
    }

    @Override
    public Course queryCourseById(String id) {
        return courseMapper.selectCourseById(id);
    }

    @Override
    public int editCourse(Course course) {
        return courseMapper.updateCourse(course);
    }

    @Override
    public int deleteCourseByIds(String[] id) {
        return courseMapper.deleteCourseByIds(id);
    }

    @Override
    public List<Course> queryAllCourses() {
        return courseMapper.selectAllCourses();
    }

    @Override
    public List<Course> queryAllCourseByIds(String[] id) {
        return null;
    }
}
