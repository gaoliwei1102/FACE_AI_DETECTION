package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Subject;

import java.util.List;
import java.util.Map;

public interface SubjectService {
    
    public List<Subject> queryAllSubjectsByCondition(Map<String,Object> map);


    int addSubject(Subject subject);

    Subject querySubjectById(String id);

    int editSubject(Subject subject);

    int deleteSubjectByIds(String[] id);

    List<Subject> queryAllSubjects();

    List<Subject> queryAllSubjectByIds(String[] id);

}
