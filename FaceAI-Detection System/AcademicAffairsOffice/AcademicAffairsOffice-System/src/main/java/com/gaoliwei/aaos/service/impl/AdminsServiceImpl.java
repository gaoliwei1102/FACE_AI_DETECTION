package com.gaoliwei.aaos.service.impl;

import com.gaoliwei.aaos.domain.Admins;
import com.gaoliwei.aaos.mapper.AdminsMapper;
import com.gaoliwei.aaos.service.AdminsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;

@Service("adminsService")
public class AdminsServiceImpl implements AdminsService {

    @Autowired
    private AdminsMapper adminsMapper;


    @Override
    public Admins queryAdminsByUsernameAndPassword(Map<String, Object> map) {
        return adminsMapper.selectAdminsByUsernameAndPassword(map);
    }
}
