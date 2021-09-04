package com.light.controllers;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.view.RedirectView;
@Controller
@ResponseStatus(HttpStatus.MOVED_PERMANENTLY)
public class AppErrorController implements ErrorController{
    private final static String PATH = "/error";
    @RequestMapping(PATH)
    @ResponseBody
    public ModelAndView getErrorPath() {
        RedirectView red = new RedirectView("/",true);
        red.setStatusCode(HttpStatus.MOVED_PERMANENTLY);
        return new ModelAndView(red);
    }

}