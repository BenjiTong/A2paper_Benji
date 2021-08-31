package com.light.controllers;


import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.light.Util.GithubConstant;
import com.light.Util.HttpsClientUtils;
import com.light.Util.HttpsUtil;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
//import org.apache.commons.lang3.StringUtils;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

@Controller
public class GithubLogController {

//    @Autowired
//    private IGithubService githubService;
    //The callback address
    @RequestMapping("/oauth/redirect")
    public String callback(String code, String state, Model model, HttpServletRequest req) throws Exception{
        System.out.println(code);
/*        public static boolean hasText(@Nullable String str) {
              return (str != null && !str.isEmpty() && containsText(str));
        }*/
        if (StringUtils.hasText(code) && StringUtils.hasText(state)){
            HttpsUtil http = new HttpsUtil();
            //Request a token through code
            String token_url = GithubConstant.TOKEN_URL.replace("CODE",code);
            //Put the String into the map
            String responseStr = http.doGetForString(token_url);
            Map<String, Object> resMap = urlStringToMap(responseStr);
            System.out.println(resMap);
            if(resMap.get("access_token")!=null){
                //            //Access Token
                String token = resMap.get("access_token").toString();
                System.out.println(token);
//
//            //Obtain user information using a Token
                String userinfo_url = GithubConstant.USER_INFO_URL.replace("TOKEN", token);
            System.out.println("用户信息===:"+userinfo_url);
            Map<String,String> header = new HashMap<>();
            header.put("Authorization","token "+token);
            responseStr = http.doGetForStringByHeader("https://api.github.com/user/repos",header);

            model.addAttribute("userInfo",JSONArray.parse(responseStr));
//            Map<String ,String > responseMap  = HttpsClientUtils.getMapByJson(responseStr);
            }

            //Login successful
            return "main";

        }


        //Return to the login page
        return "main";
    }

    public Map<String,Object> urlStringToMap(String str){
        Map<String,Object> map = new HashMap<>();
        if(str.contains("&")){
            String[] keyValueArr = str.split("&");
            Arrays.stream(keyValueArr).forEach(item ->{
                String[] keyAndValues = item.split("=");
                if(keyAndValues.length==2){
                    map.put(keyAndValues[0],keyAndValues[1]);
                }

            });
            return map;
        }else{
            if(str.contains("=")){
                String[] keyAndValues = str.split("=");
                if(keyAndValues.length==2){
                    map.put(keyAndValues[0],keyAndValues[1]);
                }
                return map;
            }else{
                return null;
            }
        }

    }


}
