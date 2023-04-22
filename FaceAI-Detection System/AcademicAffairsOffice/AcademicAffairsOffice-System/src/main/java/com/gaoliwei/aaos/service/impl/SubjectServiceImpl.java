package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Subject;
import com.gaoliwei.aaos.mapper.SubjectMapper;
import com.gaoliwei.aaos.service.SubjectService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
@Service("subjectService")
public class SubjectServiceImpl implements SubjectService {
    @Autowired
    private SubjectMapper subjectMapper;

    @Override
    public List<Subject> queryAllSubjectsByCondition(Map<String, Object> map) {
        return subjectMapper.selectAllSubjectsByCondition(map);
    }

    @Override
    public int addSubject(Subject subject) {
        return subjectMapper.insertSubject(subject);
    }

    @Override
    public Subject querySubjectById(String id) {
        return subjectMapper.selectSubjectById(id);
    }

    @Override
    public int editSubject(Subject subject) {
        return subjectMapper.updateSubject(subject);
    }

    @Override
    public int deleteSubjectByIds(String[] id) {
        return subjectMapper.deleteSubjectByIds(id);
    }

    @Override
    public List<Subject> queryAllSubjects() {
        return subjectMapper.selectAllSubjects();
    }

    @Override
    public List<Subject> queryAllSubjectByIds(String[] id) {
        return null;
    }
}
