package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Student;

import java.util.List;
import java.util.Map;

public interface StudentService {

    public List<Student> queryAllStudentsByCondition(Map<String,Object> map);


    int addStudent(Student student);

    Student queryStudentById(String id);

    int editStudent(Student student);

    int deleteStudentByIds(String[] id);

    List<Student> queryAllStudents();

    List<Student> queryAllStudentByIds(String[] id);
    
}
