function FindProxyForURL(url, host)
{
    var proxy_yes = "PROXY 127.0.0.1:8080";
    var proxy_no  = "DIRECT";

    if (shExpMatch(host, "mitm.it") || 
        shExpMatch(host, "www.tsotesting.com") || 
        shExpMatch(host, "*thesettlersonline*") || 
        shExpMatch(host, "ubistatic-a.akamaihd.net") ||
        shExpMatch(host, "tso-*-ssl.cdn.ubi.com")) { return proxy_yes; }

    return proxy_no;
}
