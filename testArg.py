#coding=utf-8

import sys
def testArg(**param):
    print param
    print type(param)
    testTuple(param['name'],param['id'],param['age'])
def testTuple(name,id=1,*param):#having-default param must at right

    print name,id,param

testArg(id=2,name="wtlwang",age=22)
testTuple(1,1,2,3,"wtl")
f=open('hello.py')
f.close()
l=['wtlwang','wtl','lianjia','test','what']
f=open('test.txt','w')
for s in l:
    f.write(s+'\n')
f.writelines(l)
f.close()
