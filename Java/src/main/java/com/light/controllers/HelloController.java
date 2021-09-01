package com.light.controllers;

import com.light.repository.MainRepository;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/")
public class HelloController {

    private final MainRepository mainRepository;
    Logger logger = LoggerFactory.getLogger(this.getClass());

    @GetMapping("/")
    public String hello(Model model, @RequestParam(value="name", required=false, defaultValue="World") String name) {
        model.addAttribute("name", name);
        long cnt = mainRepository.count();
        logger.debug("get from db:" + cnt);
        return "hello";
    }

    @Autowired
    private HelloController(MainRepository mainRepository) {
        this.mainRepository = mainRepository;
    }

}

