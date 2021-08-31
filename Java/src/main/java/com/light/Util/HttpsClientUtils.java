package com.light.Util;

import com.alibaba.fastjson.JSONObject;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.util.HashMap;
import java.util.Map;

public class HttpsClientUtils {

    public static String doGet(String url) throws Exception{

        CloseableHttpClient httpclient = HttpClients.createDefault();

        HttpGet httpGet = new HttpGet(url);

        //Sending an HTTP request
        CloseableHttpResponse response = httpclient.execute(httpGet);
        //Parsing response results
        if(response.getStatusLine().getStatusCode()==200){

            //Get the content
            HttpEntity responseEntity = response.getEntity();

            return EntityUtils.toString(responseEntity);

        }

        return null;

    }


    public static Map<String, String> getMap(String responseEntity){

        Map<String ,String > map = new HashMap<>();
        //Parse string with &
        String[] result  = responseEntity.split("\\&");
        //Store strings into a map
        for (String str : result){
            String[] split  = str.split("=");
            if (split.length == 1){
                map.put(split[0],null);
            } else {
                map.put(split[0],split[1]);
            }
        }

        return map;

    }

    public static Map<String ,String > getMapByJson(String responseEntity){

        Map<String,String> map = new HashMap<>();
        JSONObject jsonObject = JSONObject.parseObject(responseEntity);
        for(Map.Entry<String ,Object> entry : jsonObject.entrySet()){
            String key = entry.getKey();
            String value = String.valueOf(entry.getValue());
            map.put(key,value);
        }

        return map;
    }



}
