// ==UserScript==
// @name           tsohld
// @namespace      tsohld
// @description    Highlight collections on the map
// @author         wd
// @grant          none
// @version        1.2
// @include        http://www.tsotesting.com/en/play
// @include        http://www.thesettlersonline.com.br/pt/jogar
// @include        http://www.thesettlersonline.com/en/play
// @include        http://www.thesettlersonline.net/en/play
// @include        http://www.thesettlersonline.fr/fr/jouer
// @include        http://thesettlersonline.cz/cs/play
// @include        http://www.diesiedleronline.de/de/spielen
// @include        http://www.thesettlersonline.gr/el/play
// @include        http://www.thesettlersonline.it/it/gioca
// @include        http://www.juego-thesettlersonline.com/es/jugar
// @include        http://www.thesettlersonline.nl/nl/play
// @include        http://www.thesettlersonline.pl/pl/graj
// @include        http://www.thesettlersonline.ro/ro/play
// @include        http://www.thesettlersonline.ru/ru/play
// @include        http://www.thesettlersonline.es/es/jugar
// @include        http://ru.anno-online.com/ru/play
// @include        https://www.tsotesting.com/en/play
// @include        https://www.thesettlersonline.com.br/pt/jogar
// @include        https://www.thesettlersonline.com/en/play
// @include        https://www.thesettlersonline.net/en/play
// @include        https://www.thesettlersonline.fr/fr/jouer
// @include        https://thesettlersonline.cz/cs/play
// @include        https://www.diesiedleronline.de/de/spielen
// @include        https://www.thesettlersonline.gr/el/play
// @include        https://www.thesettlersonline.it/it/gioca
// @include        https://www.juego-thesettlersonline.com/es/jugar
// @include        https://www.thesettlersonline.nl/nl/play
// @include        https://www.thesettlersonline.pl/pl/graj
// @include        https://www.thesettlersonline.ro/ro/play
// @include        https://www.thesettlersonline.ru/ru/play
// @include        https://www.thesettlersonline.es/es/jugar
// ==/UserScript==


var scr=document.createElement("script");
scr.text="("+(function(){
  var c=(" "+document.cookie+";").match(" hld=(.*?);")
//  if(url=prompt("                  ?",c?c[1]:"http://127.0.0.1:9000")){
    url="http://127.0.0.1:9000"
    document.cookie="hld="+url+"; expires=Tue, 19 Jan 2038 03:14:07 GMT"
    var o=document.getElementsByName("SWMMO")[0]
    o.setAttribute("flashVars",o.getAttribute("flashVars").replace("&s=","&s="+url+"|"))
    o.outerHTML=o.outerHTML
//  }
}).toString()+")()";
document.querySelector("body").appendChild(scr);
