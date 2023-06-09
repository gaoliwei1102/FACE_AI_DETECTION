package com.gaoliwei.aaos.mapper;

import com.gaoliwei.aaos.domain.Student;
import com.gaoliwei.aaos.domain.Student;

import java.util.List;
import java.util.Map;

public interface StudentMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table student
     *
     * @mbggenerated Mon Apr 04 11:12:55 CST 2022
     */
    int deleteByPrimaryKey(String id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table student
     *
     * @mbggenerated Mon Apr 04 11:12:55 CST 2022
     */
    int insert(Student record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table student
     *
     * @mbggenerated Mon Apr 04 11:12:55 CST 2022
     */
    int insertSelective(Student record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table student
     *
     * @mbggenerated Mon Apr 04 11:12:55 CST 2022
     */
    Student selectByPrimaryKey(String id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table student
     *
     * @mbggenerated Mon Apr 04 11:12:55 CST 2022
     */
    int updateByPrimaryKeySelective(Student record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table student
     *
     * @mbggenerated Mon Apr 04 11:12:55 CST 2022
     */
    int updateByPrimaryKey(Student record);


    /**
     * 通过条件去检索所有的学生
     * @return
     */
    List<Student> selectAllStudentsByCondition(Map<String, Object> map);


    /**
     * 插入一个学生的具体信息至表格
     * @param student
     * @return
     */
    int insertStudent(Student student);


    /**
     * 通过id查询学生信息
     * @param id
     * @return
     */
    Student selectStudentById(String id);


    /**
     * 更新学生的具体的信息
     * @param student
     * @return
     */
    int updateStudent(Student student);


    /**
     * 根据id数组删除指定的学生信息
     * @param id
     * @return
     */
    int deleteStudentByIds(String[] id);


    /**
     * 检索所有的学生信息
     * @return
     */
    List<Student> selectAllStudents();


    /**
     * 通过id检索所有的学生信息
     * @param id
     * @return
     */
    List<Student> selectAllStudentByIds(String[] id);
}