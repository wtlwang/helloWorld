#!/usr/bin/python
#coding='utf-8'
#
from __future__ import generators
import time
import os
from datetime import date
import shutil

def testBool(data):
    print "bool(",data,'):'
    print '\t',bool(data)
testBool(0)
testBool(())
testBool([])
testBool({})
testBool(1)
testBool([1])

def testYield(n):
    while n>=0:
        yield n
        n-=1
print "test yield 8"
for i in testYield(8):
    print i

    
print "i'm python2.7.5"
dic={"body":{"resultSet":{"docs":"wtl"}}}
print dic["body"]["resultSet"]["docs"]
print "%s" %(dic)

print "execute global"
def local_func():
    print "excute local_func"
    
today=date.today()
todayStr=today.strftime("%Y-%m-%d")#must %Y
print todayStr
shutil.copy('E:/python27Doc/test.py','E:/')
os.remove('E:/test.py')

str1='hello,world,it\'s your world'
usrName='wangtianliang'
usrName=raw_input('please input your name\n')
str2=str1.replace('world',usrName,1)
print str2
