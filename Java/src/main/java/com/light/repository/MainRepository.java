package com.light.repository;


import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

import com.light.entity.MainObj;

@Repository
public interface MainRepository extends CrudRepository<MainObj, Long> {

    List<MainObj> findAll();
}