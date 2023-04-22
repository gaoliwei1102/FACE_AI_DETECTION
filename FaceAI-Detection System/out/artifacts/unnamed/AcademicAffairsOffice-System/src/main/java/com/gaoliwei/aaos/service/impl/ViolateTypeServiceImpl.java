package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.ViolateType;
import com.gaoliwei.aaos.mapper.ViolateTypeMapper;
import com.gaoliwei.aaos.service.ViolateTypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;


@Service("violateTypeService")
public class ViolateTypeServiceImpl implements ViolateTypeService {

    @Autowired
    private ViolateTypeMapper violateTypeMapper;

    @Override
    public List<ViolateType> queryAllViolateTypesByCondition(Map<String, Object> map) {
        return violateTypeMapper.selectAllViolateTypesByCondition(map);
    }

    @Override
    public int addViolateType(ViolateType violateType) {
        return violateTypeMapper.insertViolateType(violateType);
    }

    @Override
    public ViolateType queryViolateTypeById(String id) {
        return violateTypeMapper.selectViolateTypeById(id);
    }

    @Override
    public int editViolateType(ViolateType violateType) {
        return violateTypeMapper.updateViolateType(violateType);
    }

    @Override
    public int deleteViolateTypeByIds(String[] id) {
        return violateTypeMapper.deleteViolateTypeByIds(id);
    }

    @Override
    public List<ViolateType> queryAllViolateTypes() {
        return violateTypeMapper.selectAllViolateTypes();
    }

    @Override
    public List<ViolateType> queryAllViolateTypeByIds(String[] id) {
        return null;
    }
}
