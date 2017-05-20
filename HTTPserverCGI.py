#!/usr/bin/python3
#coding=utf-8
import cgitb
cgitb.enable()
import http.server
port=5005
serverAddr=("",port)
httpd=http.server.HTTPServer(serverAddr,http.server.CGIHTTPRequestHandler)
print("serving at port:",port)
httpd.serve_forever()

