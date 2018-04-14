# gps-tracker

A micro-service for GPS trackers Q50, Q60, 
Q80, Q90, GW100, GW100S, GW200, GW200S, GW300, GW500S, 
GW600S, GW700, GW800, GW900, GW900S, GW1000, EW100, K911, 
Titan Watch Q50


# How to use


* Figure out your PC external IP address - https://whatismyipaddress.com/
* Open port 4444 in your router NAT
* Run the script using something like

    python main.py
    
* Configure the url in the tracker device

    pw,123456,YOUR-IP-ADDRESS-HERE,4444# 


Reponse to the command:

    pw,123456,ts#
    
Looks like this:

    ver:G36_V4.0_DSPRLCD0_2015.08.15_18.40.57;
    ID:1452592xx;
    imei:359614xxxxxxxxx;
    ip_url:54.169.10.136;
    port:8001;
    center:+xxxxxxxxxxxx;
    slave: +xxxxxxxxxxxx;
    sos1:+xxxxxxxxxxxx;
    sos2:+xxxxxxxxxxxx;
    sos3:+xxxxxxxxxxxx;
    upload:7200S;
    bat level:100;
    language:0;
    zone:2.00;
    GPS:NO(0);
    GPRS:OK(100);
    pw:123456;

Report looks like this

    [3G*1452592884*0009*LK,0,0,95][3G*1452592884*006B*UD2,130418,132258,V,32.180752,N,34.8548737,E,0.00,0.0,0.0,5,100,96,0,0,00000000,1,255,425,2,33576,11402,164][3G*1452592884*00A9*UD2,130418,132308,V,32.180752,N,34.8548737,E,0.00,0.0,0.0,5,100,96,0,0,00000000,5,0,425,2,33576,11402,160,33576,12403,139,33576,11401,138,33576,11881,129,33576,11403,128][3G*1452592884*00AB*UD2,130418,132319,A,32.180439,N,34.8556061,E,1.79,207.6,0.0,5,100,96,0,0,00000000,5,0,425,2,33576,11402,159,33576,12403,139,33576,11401,137,33576,11881,129,33576,11403,128][3G*1452592884*00BB*UD2,130418,132329,A,32.180473,N,34.8555717,E,1.18,155.3,0.0,5,100,96,0,0,00000000,6,0,425,2,33576,11402,161,33576,12403,137,33576,11401,137,33552,11301,134,33576,11403,129,33576,11881,129][3G*1452592884*00BD*UD2,130418,132339,A,32.180401,N,34.8556137,E,2.37,147.4,0.0,5,100,96,0,0,00000000,6,255,425,2,33576,11402,159,33576,12403,138,33576,11401,137,33552,11301,134,33576,11403,131,33576,11881,129][3G*1452592884*00BD*UD2,130418,132349,A,32.180347,N,34.8556786,E,6.09,121.2,0.0,4,100,96,0,0,00000000,6,255,425,2,33576,11402,161,33576,12403,138,33576,11401,137,33552,11301,134,33576,11403,130,33576,11881,128][3G*1452592884*00BB*UD2,130418,132359,A,32.180302,N,34.8557549,E,3.70,119.8,0.0,4,100,96,0,0,00000000,6,0,425,2,33576,11402,161,33576,11401,145,33576,12403,138,33552,11301,135,33576,11403,130,33576,11881,129][3G*1452592884*00BD*UD2,130418,132409,A,32.180283,N,34.8557472,E,1.98,237.1,0.0,4,100,96,0,0,00000000,6,255,425,2,33576,11402,162,33576,11401,145,33576,12403,138,33552,11301,135,33576,11403,131,33576,11881,129][3G*1452592884*00CD*UD2,130418,132419,A,32.180275,N,34.8557434,E,1.66,299.7,0.0,4,100,96,0,0,00000000,7,255,425,2,33576,11402,160,33576,11401,143,33576,12403,138,33552,11301,135,33576,11403,131,33576,11884,131,33576,11881,128][3G*1452592884*00CD*UD2,130418,132424,A,32.180290,N,34.8557167,E,1.72,283.1,0.0,4,100,96,0,0,00000000,7,255,425,2,33576,11402,161,33576,11401,138,33576,12403,138,33552,11301,135,33576,11403,129,33576,11881,128,33576,11884,127][3G*1452592884*005F*UD2,130418,133556,V,32.180290,N,34.8557167,E,0.00,0.0,0.0,0,100,50,0,0,00000000,1,0,0,0,0,0,110][3G*1452592884*006B*UD2,130418,133606,V,32.180290,N,34.8557167,E,0.00,0.0,0.0,3,100,95,0,0,00000000,1,255,425,2,33576,11402,161][3G*1452592884*006B*UD2,130418,133616,V,32.180290,N,34.8557167,E,0.00,0.0,0.0,6,100,95,0,0,00000000,1,255,425,2,33576,11402,162][3G*1452592884*00BB*UD2,130418,133626,A,32.180714,N,34.8545227,E,3.76,310.4,0.0,7,100,95,0,0,00000000,6,0,425,2,33576,11402,161,33576,11401,139,33576,12403,137,33576,13862,130,33576,11881,128,33576,11403,128][3G*1452592884*00BB*UD2,130418,133637,A,32.180344,N,34.8553391,E,0.63,279.3,0.0,6,100,94,0,0,00000000,6,0,425,2,33576,11402,161,33576,12403,138,33576,11401,135,33576,11403,131,33576,13862,131,33576,11881,129][3G*1452592884*00BB*UD2,130418,133647,A,32.180344,N,34.8553658,E,2.48,265.0,0.0,6,100,94,0,0,00000000,6,0,425,2,33576,11402,161,33576,11401,141,33576,12403,139,33576,13862,131,33576,11403,129,33576,11881,128][3G*1452592884*00CB*UD2,130418,133657,A,32.180355,N,34.8553391,E,1.70,257.4,0.0,6,100,94,0,0,00000000,7,0,425,2,33576,11402,161,33576,11401,139,33576,12403,139,33552,11301,136,33576,13862,131,33576,11403,129,33576,11881,129][3G*1452592884*00CD*UD2,130418,133707,A,32.180344,N,34.8553047,E,1.50,247.1,0.0,6,100,95,0,0,00000000,7,255,425,2,33576,11402,161,33576,11401,141,33576,12403,138,33552,11301,136,33576,13862,131,33576,11403,129,33576,11881,128][3G*1452592884*00CD*UD2,130418,133717,A,32.180332,N,34.8553009,E,0.44,212.9,0.0,6,100,95,0,0,00000000,7,255,425,2,33576,11402,162,33576,11401,140,33576,12403,137,33552,11301,135,33576,13862,130,33576,11881,128,33576,11403,127][3G*1452592884*00BB*UD2,130418,133727,A,32.180313,N,34.8553162,E,0.63,171.7,0.0,6,100,95,0,0,00000000,6,0,425,2,33576,11402,162,33576,11401,139,33576,12403,138,33552,11301,135,33576,13862,130,33576,11881,129][3G*1452592884*00CD*UD2,130418,133737,A,32.180298,N,34.8553162,E,0.44,182.8,0.0,6,100,95,0,0,00000000,7,255,425,2,33576,11402,160,33576,11401,139,33576,12403,138,33552,11301,135,33576,13862,129,33576,11881,129,33576,11403,126][3G*1452592884*00CD*UD2,130418,133747,A,32.180290,N,34.8553123,E,0.37,233.9,0.0,6,100,95,0,0,00000000,7,255,425,2,33576,11402,161,33576,12403,139,33576,11401,139,33552,11301,135,33576,16283,131,33576,13862,129,33576,11881,129][3G*1452592884*00CD*UD2,130418,133752,A,32.180347,N,34.8551140,E,2.78,278.5,0.0,6,100,95,0,0,00000000,7,255,425,2,33576,11402,161,33576,12403,139,33576,11401,138,33552,11301,135,33576,16283,131,33576,13862,129,33576,11881,129][3G*1452592884*0009*LK,0,0,95]






Links

*  https://www.gpswox.com/en/supported-gps-trackers/watch/jm09-q50-children-watch
*  https://github.com/freshworkstudio/gps-tracking-nodejs/issues/17
*  http://livegpstracks.com/forum/viewtopic.php?p=6483#p6483


