#
import sys
from pprint import pprint
dic={}
if len(sys.argv) <2:
    filename=raw_input('input the filename:')
else:
    filename=sys.argv[1]

f=open(filename)
for s in f.readlines():
    try:
        name,course,score=s.split()
    except ValueError:
        continue
 #   if name is not '':
 
    try:
        dic[name]+=int(score)
    except KeyError:
        dic.setdefault(name,int(score))
print 'wtl','eng',  #without '\n'
print 80
f.close()
pprint(dic)
