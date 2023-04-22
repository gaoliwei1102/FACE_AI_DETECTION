package com.gaoliwei.aaos.service;

import com.gaoliwei.aaos.domain.Admins;

import java.util.Map;

public interface AdminsService {

    public Admins queryAdminsByUsernameAndPassword(Map<String, Object> map);
}
