package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Violate;

import java.util.List;
import java.util.Map;

public interface ViolateService {

    public List<Violate> queryAllViolatesByCondition(Map<String,Object> map);


    int addViolate(Violate violate);

    Violate queryViolateById(String id);

    int editViolate(Violate violate);

    int deleteViolateByIds(String[] id);

    List<Violate> queryAllViolates();

    List<Violate> queryAllViolateByIds(String[] id);

}
