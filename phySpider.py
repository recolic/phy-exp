#!/bin/env python3
# -*- coding: UTF-8 -*-
# Scan if there's any empty seat to play physics exp..
# By Recolic Keghart, Apr 26, 2017

import urllib.parse, urllib.request
import sys

#weekNumberList = [14,15,16,17,18]
#experimentNumberList = [37,38,39,40,41,42,43,44]
weekNumberList = [12,13,14,15,16,17]
experimentNumberList = [52,53,54,55,56,57,58,59]


errorPageDump = '/home/recolic/tmp/phySpiderDump.html'

# Needn't edit below.
experimentNumberDict = {
    57:'稳态测固体导热系数',
    59:'电路的暂态过程',
    58:'音叉实验',
    56:'扭摆测转动惯量',
    54:'光电效应',
    52:'液体张力',
    53:'偏振双折射',
    55:'组合光学'
    }


def doLogin():
    cookieStr = ''
    print('Please use --cookie')
    exit(1)
    return cookieStr

def dumpWebpage(content, filePath):
    fd = open(filePath, 'w')
    fd.write(content)
    fd.close()

def doTest(expNum, weekNum, cookieStr):
    url='http://115.156.233.249/yuyue.asp'
    formData = urllib.parse.urlencode({
        'ExperimentSelectCtrl':expNum, 
        'hidden_sybh':expNum, 
        'zc':weekNum, 
        'hidden_zc':weekNum, 
        'hidden_ActionType':0, 
        'hidden_DiscardYuYue_sbbh':0, 
        'hidden_DiscardYuYue_zc':0, 
        'hidden_DiscardYuYue_rq':0, 
        'hidden_Msg':None
    }).encode('utf-8')
    request = urllib.request.Request(url, headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'166',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':cookieStr,
        'Host':'115.156.233.249',
        'Origin':'http://115.156.233.249',
        'Referer':'http://115.156.233.249/yuyue.asp',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    })
    responce = urllib.request.urlopen(request, formData)
    responce = responce.read().decode('utf-8', errors = 'backslashreplace')
    if len(responce) < 3000:
        if responce.find('<head><title>Object moved<') != -1:
            print('Error: Cookie is invalid. Responce dumped at ', errorPageDump)
        if responce.find('<META NAME="GENERATOR" Content="Microsoft Visual Studio 6.0">') != -1:
            print('Error: Cookie is invalid. Responce dumped at ', errorPageDump)
        else:
            print('Error: Unknown error. Responce dumped at ', errorPageDump)
        dumpWebpage(responce, errorPageDump)
        exit(1)
    location = 10000
    while True:
        location = responce.find('<input type=\'radio\' name=\'RadioButton_yuyue\'', location + 1)
        if location != -1:
            location += 52
            seatStr = responce[location:location+9]
            print('Available seat detected:', experimentNumberDict[expNum], 'week=', weekNum, 'seat=', seatStr)
        else:
            #print('Full:', experimentNumberDict[expNum], ',week=', weekNum)
            break
    return


# login:
if len(sys.argv) > 1 and sys.argv[1] == '--cookie':
    try:
        with open('cookie.in', 'r') as cookieFile:
            m_cookie = cookieFile.readline()
            if m_cookie[len(m_cookie) - 1] == '\n':
                m_cookie=m_cookie[0:len(m_cookie)-2]
    except FileNotFoundError:
        print('Please input a valid cookie(You can put it as cookie.in):')
        m_cookie = input()
    print('Using cookie:', m_cookie)
else:
    m_cookie = doLogin()
print('\nStart working now...\n')

for expNum in experimentNumberList:
    for weekNum in weekNumberList:
        doTest(expNum, weekNum, m_cookie)

