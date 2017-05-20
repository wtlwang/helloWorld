#coding=utf8
import sys
import socket
print(sys.argv[0],len(sys.argv))
fi=open(sys.argv[1],'rb')
bytess=fi.read()
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host='222.20.94.67'#102
port=8082
addr=(host,port)

s.sendto(bytes(sys.argv[1],'utf8'),addr)
by,add=s.recvfrom(65536)
s.sendto(bytess,addr)

ip,p=addr
print(by.decode('utf8')+"\nget Data from "+ip,':',p)

s.close()	
