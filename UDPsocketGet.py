#coding=utf8
import sys
import socket
print(sys.argv[0],len(sys.argv))
#fi=open(sys.argv[1],'rb')
#bytess=fi.read()
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host='222.20.94.219'#67'
port=8082
addr=(host,port)

s.sendto(bytes(sys.argv[1],'utf8'),addr)
#s.sendto(bytess,addr)

#by,addr=s.recvfrom(1024)
#ip,p=addr
#print("get file: "+by.decode('utf8')+"\nfrom "+ip,':',p)

fname=(sys.argv[1])
f=open(fname,'wb')
by,addr=s.recvfrom(65536)
f.write(by)
f.close()
s.sendto(b"Yes! I Got the file: "+bytes(fname,'utf8'),addr)
print("get the file",fname)

s.close()	
