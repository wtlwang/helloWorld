#coding=utf8
import sys
import socket
print(sys.argv[0],len(sys.argv))



SND_BUF_SIZE=1024*1024
RCV_BUF_SIZE=1024*1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='222.20.94.67'#102
port=8083
addr=(host,port)
defBufSize=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
print("the default send buffer size is :",defBufSize)
defBufSize=s.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
print("the default receive buffer size is :",defBufSize)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SND_BUF_SIZE)
s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RCV_BUF_SIZE)
defBufSize=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
print("the send buffer size now is :",defBufSize)
defBufSize=s.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
print("the receive buffer size now is :",defBufSize)


for i in range(1,len(sys.argv)):
	fi=open(sys.argv[i],'rb')
	bytess=fi.read()
	fi.close()
	print("the file length is: ",len(bytess),"bytes")
	s.connect(addr)
	fname=sys.argv[i]
	fname=(fname.split('/'))[-1]
	fname.encode('utf-8')
	sendNum=s.send(bytes(fname,'utf8'))
	by=s.recv(1024)
	#if not by:
	#	by=s.recv(2048)
	sendNum=s.send(bytess)
	print("send ",sendNum,"bytes data")

	by=s.recv(65536)
	ip,p=addr
	print("\t\t"+by.decode('utf8')+"\nget response from "+ip,':',p,'\n')
	s.close()
	s=socket.socket()
	s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SND_BUF_SIZE)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RCV_BUF_SIZE)
s.close()
		
