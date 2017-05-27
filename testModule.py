from __future__ import generators
import os
import sys

#print sys.path
#print os.path
filename= 'hello.py'
print filename[0:-2]
print filename[:-3:-1]#add : before; reverse the string
script=open(filename)
for s in script.readlines():
    if s.startswith('def'):
        print s.split()[1].rstrip(':')
    if s.startswith('class'):
        
        print s.split()[1].split(':')[0]
        print '\t',s
        
script.close()
def fun(args):
    print "first call"
    yield 1
    print "second call"
    print "args is: "+str(args)
   
    yield 2

for n in fun(1):
    print n
for n in fun(2):
    print n
