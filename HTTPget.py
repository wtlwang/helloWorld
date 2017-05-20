#!/usr/bin/python3 
#coding=utf-8
 # This creates an HTTP message
 # with the content of BODY as the enclosed representation
 # for the resource http://localhost:8080/file
 
import http.client
import sys
#BODY = "***filecontents***"
#urlAll=sys.argv[1]
#http://222.20.94.19:5005/139.199.189.194:5005/cgi-bin/file/hust.html
def urlGet(urlAll):
    sign=urlAll.partition(':')[0]

    if sign=='https':
        urlHost=urlAll.replace('https://','',1)
    else:
        urlHost=urlAll.replace('http://','',1)

    host=urlHost.partition('/')[0]
    #host="115.156.188.226"
    if sign=='http':
        conn = http.client.HTTPConnection(host)
    else:
        conn = http.client.HTTPSConnection(host)
        

    url=urlHost.replace(host,'',1)
    #url="/act.sccnn.com/cdtvt/8sc/042/22580few.rar"
    conn.request("GET",url)
    response = conn.getresponse()
    print(response.status, response.reason,response.version,response.fileno())
    print(response.getheaders())
    data=response.read()
    return data,urlHost
if len(sys.argv)>1:
    urlAll=sys.argv[1]
else:
    urlAll=input("input the url(http(s)?):\n")
    
data,urlHost=urlGet(urlAll)
if len(sys.argv)>2:
    filename=sys.argv[2]
else:
    filename=urlHost.split('/')[-1]
if not filename:
    filename='material.rar'
file=open(filename,'wb')
file.write(data)
file.close()

print("data is saved in ",filename)

