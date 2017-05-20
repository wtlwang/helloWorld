#coding=utf-8
import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lhost=''
lport=8082
laddr=(lhost,lport)
r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#r.bind(laddr)

host='139.199.189.194'#'222.20.94.118'#
port=8082
addr=(host,port)

def mysend(addr):
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while 1:
        data=input()
        s.sendto(bytes(data,'utf8'),addr)
    s.close()


def myrecv(laddr):
    r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    r.bind(laddr)
    while 1:
        by,addr=r.recvfrom(65536)
        print('\t\t\t'+by.decode())
    r.close()

thSend=threading.Thread(target=mysend,name="send",args=(addr,))
thRecv=threading.Thread(target=myrecv,name='recv',args=(laddr,))

thSend.start()
thRecv.start()

s.close()
r.close()

    
    
