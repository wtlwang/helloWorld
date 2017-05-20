#coding=utf-8
import socket
import threading

#s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lhost=''
lport=8088
laddr=(lhost,lport)
#r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#r.bind(laddr)

host='139.199.189.194'#'222.20.94.118'#
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
    try:
    	r.bind(laddr)
    except OSError:
        laddr=laddr[0],laddr[1]+1001
        r.bind(laddr)
    global addr
    r.sendto(bytes(str(laddr[1]),'utf-8'),addr)
    by,address=r.recvfrom(1024)
    print(str(address)+':'+str(by))
    addr=addr[0],int(by)
    thSend=threading.Thread(target=mysend,name="send",args=(addr,))
    thSend.start()
    while 1:
        by,addr=r.recvfrom(65536)
        print('\r'+str(addr)+':'+by.decode()+'\n\r\t\t\t\t\t',end='')
        #print('\r\t\t\t\t\t',end='')
    r.close()


thRecv=threading.Thread(target=myrecv,name='recv',args=(laddr,))


thRecv.start()

#s.close()
#r.close()

    
    
