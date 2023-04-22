package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Course;

import java.util.List;
import java.util.Map;

public interface CourseService {

    public List<Course> queryAllCoursesByCondition(Map<String,Object> map);


    int addCourse(Course course);

    Course queryCourseById(String id);

    int editCourse(Course course);

    int deleteCourseByIds(String[] id);

    List<Course> queryAllCourses();

    List<Course> queryAllCourseByIds(String[] id);
    
}
