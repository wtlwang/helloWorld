#!/usr/bin/python3
#coding=utf-8
import os
Rhost=os.getenv("REMOTE_HOST")
Raddr=os.getenv("REMOTE_ADDR")
method=os.getenv("REQUEST_METHOD")
RecvType=os.getenv("CONTENT_TYPE")
accencoding=os.getenv("ACCEPT_ENCODING")

print("Content-type: text/html;charset=utf-8")
print()

fin=open('./index.html','r',encoding='utf-8')
data=fin.read()
print("hello,",Rhost,"your ip is: ",Raddr)
print("your request method is: ",method,"?\n")
if RecvType:
	print("your content_type is: ",RecvType)
print("do you encoding in",accencoding,"?\n")
print("do you query?: ",os.getenv("QUERY_STRING"))

print("the content length is: ",os.getenv("CONTENT_LENGTH"))
print(data)

