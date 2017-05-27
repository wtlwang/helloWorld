# coding=utf-8
import urllib2
import urllib
params={"statDate": "2017-05-16",
        "cityCode": 110000,
     #   "type": 2
        }
url="http://172.30.13.76:9014/api/qc/fake/house/identify?"+\
     urllib.urlencode(params)
print url
headers={
    'version':'v1',
    'token':'089953800829438'
    }
req=urllib2.Request(url,headers=headers)
f=urllib2.urlopen(req)
print f.getcode()
print f.info()
print f.geturl()
print U"你好"
print f.read().decode('utf-8')

def cls(object):
    def __init__(self):
        print "__init__"
    def spp(self):
        print "i'm a class"
print urllib.__dict__.keys()
