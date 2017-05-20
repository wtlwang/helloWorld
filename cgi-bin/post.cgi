#!/usr/bin/python3
#coding=utf-8
#data=input()
import os
import sys
import io
sys.stdin=io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')
#sys.setdefaultencoding('utf-8')
#import locale
#locale.getpreferredencoding()
rawfile=input()
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

file=open(filename,'wb')
#file.write(data)
print("Content-type:text/plain")
print()

while 1:
    data=input()
    #file.write(data+'\n')
    if data== "##END":	
        break
    file.write((data+'\n').encode('utf-8'))
file.close()

print("thanks ")

