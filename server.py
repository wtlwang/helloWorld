#coding=utf-8
import socket

Host=''
Port=8080
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((Host,Port))
	s.listen(1)
	conn,addr=s.accept()
	print('Got connection from',addr)
	data=conn.recv(1024)
	while 1:
		print(data)
		data=conn.recv(1024)
		if not data:break
		
	#s.send(b'thanks')
	s.close()

