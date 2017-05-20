#coding=utf8
import socket
s=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
host=''
port=8083
addr=(host,port)
s.bind(addr)
s.listen(5)
print("listening at: ",port)
while(1):
	c,addr=s.accept()
	print("get connection from",addr)
	by=c.recv(1024)
	c.send(b'None')
	filename=by.decode('utf8')
	f=open(filename,'wb')
	print("Got file:",filename)
	data=c.recv(65536)
	f.write(data)
	f.close()
	c.send(by+b' is received: '+bytes(str(len(data)),'utf8'))
	c.close()
s.close()

	
	
