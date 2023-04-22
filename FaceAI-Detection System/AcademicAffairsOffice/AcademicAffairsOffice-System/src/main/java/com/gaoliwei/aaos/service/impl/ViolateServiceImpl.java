package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Violate;
import com.gaoliwei.aaos.mapper.ViolateMapper;
import com.gaoliwei.aaos.service.ViolateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service("violateService")
public class ViolateServiceImpl implements ViolateService {

    @Autowired
    private ViolateMapper violateMapper;

    @Override
    public List<Violate> queryAllViolatesByCondition(Map<String, Object> map) {
        return violateMapper.selectAllViolatesByCondition(map);
    }

    @Override
    public int addViolate(Violate violate) {
        return violateMapper.insertViolate(violate);
    }

    @Override
    public Violate queryViolateById(String id) {
        return violateMapper.selectViolateById(id);
    }

    @Override
    public int editViolate(Violate violate) {
        return violateMapper.updateViolate(violate);
    }

    @Override
    public int deleteViolateByIds(String[] id) {
        return violateMapper.deleteViolateByIds(id);
    }

    @Override
    public List<Violate> queryAllViolates() {
        return violateMapper.selectAllViolates();
    }

    @Override
    public List<Violate> queryAllViolateByIds(String[] id) {
        return null;
    }
}
