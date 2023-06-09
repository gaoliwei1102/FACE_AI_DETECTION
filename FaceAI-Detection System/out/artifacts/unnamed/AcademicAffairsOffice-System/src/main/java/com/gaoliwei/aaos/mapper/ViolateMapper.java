package com.gaoliwei.aaos.mapper;

import com.gaoliwei.aaos.domain.Violate;
import com.gaoliwei.aaos.domain.Violate;

import java.util.List;
import java.util.Map;

public interface ViolateMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate
     *
     * @mbggenerated Tue Apr 12 13:13:06 CST 2022
     */
    int deleteByPrimaryKey(String id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate
     *
     * @mbggenerated Tue Apr 12 13:13:06 CST 2022
     */
    int insert(Violate record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate
     *
     * @mbggenerated Tue Apr 12 13:13:06 CST 2022
     */
    int insertSelective(Violate record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate
     *
     * @mbggenerated Tue Apr 12 13:13:06 CST 2022
     */
    Violate selectByPrimaryKey(String id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate
     *
     * @mbggenerated Tue Apr 12 13:13:06 CST 2022
     */
    int updateByPrimaryKeySelective(Violate record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table violate
     *
     * @mbggenerated Tue Apr 12 13:13:06 CST 2022
     */
    int updateByPrimaryKey(Violate record);


    /**
     * 通过条件去检索所有的违规
     * @return
     */
    List<Violate> selectAllViolatesByCondition(Map<String, Object> map);


    /**
     * 插入一个违规的具体信息至表格
     * @param violate
     * @return
     */
    int insertViolate(Violate violate);


    /**
     * 通过id查询违规信息
     * @param id
     * @return
     */
    Violate selectViolateById(String id);


    /**
     * 更新违规的具体的信息
     * @param violate
     * @return
     */
    int updateViolate(Violate violate);


    /**
     * 根据id数组删除指定的违规信息
     * @param id
     * @return
     */
    int deleteViolateByIds(String[] id);


    /**
     * 检索所有的违规信息
     * @return
     */
    List<Violate> selectAllViolates();


    /**
     * 通过id检索所有的违规信息
     * @param id
     * @return
     */
    List<Violate> selectAllViolateByIds(String[] id);

}