package com.gaoliwei.aaos.mapper;

import com.gaoliwei.aaos.domain.ViolateType;
import com.gaoliwei.aaos.domain.ViolateType;

import java.util.List;
import java.util.Map;

public interface ViolateTypeMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate_type
     *
     * @mbggenerated Tue Apr 12 10:49:50 CST 2022
     */
    int deleteByPrimaryKey(String id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate_type
     *
     * @mbggenerated Tue Apr 12 10:49:50 CST 2022
     */
    int insert(ViolateType record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate_type
     *
     * @mbggenerated Tue Apr 12 10:49:50 CST 2022
     */
    int insertSelective(ViolateType record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate_type
     *
     * @mbggenerated Tue Apr 12 10:49:50 CST 2022
     */
    ViolateType selectByPrimaryKey(String id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate_type
     *
     * @mbggenerated Tue Apr 12 10:49:50 CST 2022
     */
    int updateByPrimaryKeySelective(ViolateType record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate_type
     *
     * @mbggenerated Tue Apr 12 10:49:50 CST 2022
     */
    int updateByPrimaryKey(ViolateType record);


    /**
     * 通过条件去检索所有的违规种类
     * @return
     */
    List<ViolateType> selectAllViolateTypesByCondition(Map<String, Object> map);


    /**
     * 插入一个违规种类的具体信息至表格
     * @param violateType
     * @return
     */
    int insertViolateType(ViolateType violateType);


    /**
     * 通过id查询违规种类信息
     * @param id
     * @return
     */
    ViolateType selectViolateTypeById(String id);


    /**
     * 更新违规种类的具体的信息
     * @param violateType
     * @return
     */
    int updateViolateType(ViolateType violateType);


    /**
     * 根据id数组删除指定的违规种类信息
     * @param id
     * @return
     */
    int deleteViolateTypeByIds(String[] id);


    /**
     * 检索所有的违规种类信息
     * @return
     */
    List<ViolateType> selectAllViolateTypes();


    /**
     * 通过id检索所有的违规种类信息
     * @param id
     * @return
     */
    List<ViolateType> selectAllViolateTypeByIds(String[] id);


}