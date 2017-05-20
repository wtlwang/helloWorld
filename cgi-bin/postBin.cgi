#!/usr/bin/python3
#coding=utf-8
#data=input()
import os
import sys
import urllib.parse
#import cgi
import io
def ispass(passwd):
	if passwd == b"wtlwang\n":
                return True
	else:
                return False
print("Content-type:text/plain")#html")
print()
dic=os.environ
print(dic["REMOTE_ADDR"])
print(dic["QUERY_STRING"])
print(dic["CONTENT_LENGTH"])
print(dic)
#sys.stdin=io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')
#sys.setdefaultencoding('utf-8')
dicc=urllib.parse.parse_qs(dic["QUERY_STRING"])
rawfile=dicc['name'][0]

if ':' in rawfile:
	filename=rawfile.partition(':')[-1]
else:
	filename=rawfile
if filename[0]=='/':
	filename="./file"+filename
else:
	filename="./file/"+filename
filepath=os.path.dirname(filename)
if not os.path.exists(filepath):
	os.makedirs(filepath)
#filename=filename.split('/')[-1]
#filename=filename.split('\\')[-1]
if dic["CONTENT_LENGTH"]!='':
	lenth=int(dic["CONTENT_LENGTH"])
else:
	lenth=0

fin=sys.stdin.buffer

if lenth is 0:
	data=None
else:
	password=fin.readline(10)
	data=fin.read(lenth-len(password))#this is very important;
if not data:
	print("data is none")
else:
	#filename="./file/"+filename
        if ispass(password):
	        f=open(filename,'wb')
	        f.write(data)
	        f.close()
        else:
                print("your password is wrong, post failed")
fin.close()
#f.write(data)
#f.close()

print("thanks ")




