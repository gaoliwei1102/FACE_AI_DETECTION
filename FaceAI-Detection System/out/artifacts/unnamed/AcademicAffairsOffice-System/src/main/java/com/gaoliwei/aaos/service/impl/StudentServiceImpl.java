package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Student;
import com.gaoliwei.aaos.mapper.StudentMapper;
import com.gaoliwei.aaos.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service("studentService")
public class StudentServiceImpl implements StudentService {

    @Autowired
    private StudentMapper studentMapper;


    @Override
    public List<Student> queryAllStudentsByCondition(Map<String, Object> map) {
        return studentMapper.selectAllStudentsByCondition(map);
    }

    @Override
    public int addStudent(Student student) {
        return studentMapper.insertStudent(student);
    }

    @Override
    public Student queryStudentById(String id) {
        return studentMapper.selectStudentById(id);
    }

    @Override
    public int editStudent(Student student) {
        return studentMapper.updateStudent(student);
    }

    @Override
    public int deleteStudentByIds(String[] id) {
        return studentMapper.deleteStudentByIds(id);
    }

    @Override
    public List<Student> queryAllStudents() {
        return studentMapper.selectAllStudents();
    }

    @Override
    public List<Student> queryAllStudentByIds(String[] id) {
        return null;
    }
}
