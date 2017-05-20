#coding=utf-8
import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lhost=''
lport=8082
laddr=(lhost,lport)
r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#r.bind(laddr)

host='222.20.94.19'
port=8082
addr=(host,port)

def mysend(addr):
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while 1:
        data=input('\r\t\t\t\t\t')
        s.sendto(bytes(data,'utf8'),addr)
    s.close()


def myrecv(laddr):
    r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    r.bind(laddr)
    by,address=r.recvfrom(1024)
    print(str(address)+':'+str(by))
    global addr
    addr=(addr[0],int(by))
    #print(addr)
    rr=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    rr.bind(('',60000))
    rr.sendto(bytes(str(60000),'utf-8'),addr)
    thSend=threading.Thread(target=mysend,name='Send',args=(addr,))
    thSend.start()
    while 1:
        by,address=rr.recvfrom(65536)
        print('\r'+str(address)+':',by.decode())
        print('\r\t\t\t\t\t',end='')
    rr.close()
    r.close()

#thSend=threading.Thread(target=mysend,name="send",args=(addr,))
thRecv=threading.Thread(target=myrecv,name='recv',args=(laddr,))

#thSend.start()
thRecv.start()

s.close()
r.close()

    
   
