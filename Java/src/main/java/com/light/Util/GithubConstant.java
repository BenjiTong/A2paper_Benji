package com.light.util;

public class GithubConstant {

    public static final String CLIENT_ID="c04fa22c7aa981ba6419";

    public static final String CALLBACK = "http://localhost:8888/oauth/redirect";

    public static final String CODE_URL = "https://github.com/login/oauth/authorize?client_id="+CLIENT_ID+"state=STATE&redirect_uri="+CALLBACK+"";

    public static final String TOKEN_URL = "https://github.com/login/oauth/access_token?client_id="+CLIENT_ID+"&client_secret=CLIENT_SECRET&code=CODE&redirect_uri="+CALLBACK+"";

    public static final String USER_INFO_URL = "https://api.gihub.com/user/repos?access_token=TOKEN";

}

