package com.light;

import com.light.util.HttpsUtil;

public class Test {
    public static void main(String[] args) throws Exception {
        HttpsUtil http = new HttpsUtil();
        String str = http.doGetForString("https://api.github.com/user/repos?access_token=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");
        System.out.println(str);
    }
}
