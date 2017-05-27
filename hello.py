#coding=utf-8
import os.path
import sys

print os.path.abspath(sys.argv[0])
print os.path.abspath(os.path.dirname(os.__file__))
print __name__
name = 'wtlwagn'
age = 26
dictt={
    name : age
    }
print dictt
print 'hello,world','\n'

class Test(object):# python class has default __init__ function
    def __init__(self,*args):
        print "init with ",args
        
    def __del__(self):
        print "Test's object ",self,"is killed\n"

t1=Test('wtl',1,2,3,'w');

path = os.path.expanduser('~')
print path,'\n'
del(t1)


dict1= {'content-type': 'application/json', 'sample':'head_param', 'User-Agent': 'getman'}
dict2={"content-type": "application/xml",'name':'wtl'}
print dict1.values()
dict1.update(dict2)
def func(**argv):
    print argv
    print "end"
func (**dict1)

def testTuple(*args):
    data= {
            "name":"wtlwang",
            "age": 23
            }
    print data
    print args
    print "**************"

testTuple(*dict2.keys())#* means  dereference  
dictMerged1=dict(dict1.items()+dict2.items())
print dictMerged1
dictMerged2=dict(dict1, **dict2)
print dictMerged2

def testEqualNone(data):
    if data == None:
        print data,'==None'
    else:
        print data,'!=None'

testEqualNone([])
testEqualNone({})
