package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.ViolateType;

import java.util.List;
import java.util.Map;

public interface ViolateTypeService {
    
    public List<ViolateType> queryAllViolateTypesByCondition(Map<String,Object> map);


    int addViolateType(ViolateType violateType);

    ViolateType queryViolateTypeById(String id);

    int editViolateType(ViolateType violateType);

    int deleteViolateTypeByIds(String[] id);

    List<ViolateType> queryAllViolateTypes();

    List<ViolateType> queryAllViolateTypeByIds(String[] id);
    
}
