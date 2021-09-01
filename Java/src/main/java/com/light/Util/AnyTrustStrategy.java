package com.light.util;

import org.apache.http.ssl.TrustStrategy;

class AnyTrustStrategy implements TrustStrategy {

    @Override
    public boolean isTrusted(java.security.cert.X509Certificate[] chain, String authType)
            throws java.security.cert.CertificateException {
        return true;
    }

}
