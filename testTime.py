import time
tstamp=time.time()
print tstamp
ct=time.ctime(tstamp)
print ct

localt=time.localtime()
print localt

utc=time.gmtime()
print utc
print "today is 周",utc.tm_wday+1

clc=time.clock()
print clc
