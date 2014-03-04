#!/usr/bin/env python
#coding=utf-8

import cookielib
import urllib
import urllib2
import json
import re
import time

def fetion(weather_msg = "no data"):
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    t = time.localtime()
    print t.tm_year,t.tm_mon,t.tm_mday
    print "logining"
    urlbase = "http://f.10086.cn/im5/" 
    response_text = urllib2.urlopen(urlbase)
    response_text = response_text.read()
    partten = re.compile(r'login/login\.action\?mnative=\d&t=\d+')
    urlplus = partten.search(response_text)
    urlcomplete = urlbase + urlplus.group(0)
#    print urlcomplete
    qheader = {'Referer':urlcomplete}
    args = {'m':'15129245130','pass':'a251125'}
    logurl = "http://f.10086.cn/im5/login/loginHtml5.action"
    req = urllib2.Request(logurl,urllib.urlencode(args),qheader)
    jump = opener.open(req)
    page = jump.read()
#    print page
    page = json.loads(page)

    sendmsgurl = "http://f.10086.cn/im5/chat/sendNewGroupShortMsg.action"
    msg_data = {"touserid":page["idUser"],"msg":weather_msg}
    msg_back = urllib2.Request(sendmsgurl,urllib.urlencode(msg_data),qheader)
    msg_jump = opener.open(msg_back)
    msguse = msg_jump.read()
    msguse = json.loads(msguse)
    if msguse["info"] == u"发送成功":
        print "send successfully"
    else:
        print msguse
        print "send failed"
if __name__ == "__main__":
    fetion()

