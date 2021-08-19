package com.light.controllers;

import java.util.Map;
 
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class HelloWorldController {
	private String message = "Hello World";
 
	@GetMapping("/")
	public String welcome(Map<String, Object> model) {
		model.put("message", this.message);
		return "HelloWorld";
	}
}
