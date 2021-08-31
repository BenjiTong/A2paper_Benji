package com.light.Util;

public class GithubConstant {

    public static final String CLIENT_ID="952b74100002a9ff5430";

    public static final String CLIENT_SECRET="b7021233ca275c55c68dd1b19b3702b20e871dc3";

    public static final String CALLBACK = "http://localhost:8888/oauth/redirect";

    public static final String CODE_URL = "https://github.com/login/oauth/authorize?client_id="+CLIENT_ID+"state=STATE&redirect_uri="+CALLBACK+"";

    public static final String TOKEN_URL = "https://github.com/login/oauth/access_token?client_id="+CLIENT_ID+"&client_secret="+CLIENT_SECRET+"&code=CODE&redirect_uri="+CALLBACK+"";

    public static final String USER_INFO_URL = "https://api.gihub.com/user/repos?access_token=TOKEN";

}

