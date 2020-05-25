#!/usr/bin/python
#coding=utf-8
import urllib2
import os.path

def getCode(url):
    status_Code = 0
    try:
        html = urllib2.urlopen(url)
        status_Code = html.code
    except Exception,e:
        status_Code = hasattr(e,'code') and e.code
    return status_Code
def getDomain():
    print "请输入域名或IP："
    domain = raw_input()
    return domain
def dirScan():
    domain = ''
    path = ''
    domain = getDomain()
    domain = domain if domain.lower().startswith('http') else "http://"+domain
    print "请导入字典："
    path = raw_input()
    show_Code = [200, 301, 405]
    file = open(path,"r")
    while 1:
        data = file.readline()
        url = domain + data
        for x in show_Code:
            if getCode(url) == x:
                print url, x
        if not data:
            break
    file.close()
pass
dirScan()
