#coding=utf-8
import sys
import socket
print(sys.argv[0],len(sys.argv))



SND_BUF_SIZE=1024*1024
RCV_BUF_SIZE=1024*1024
SND_SIZE=65536
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.1.101" #"123.118.208.48"#"222.20.94.219" #102
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


def TCPsend(s,addr,filename):
        fi=open(filename,'rb')
        bytess=fi.read(65536)
        count=0
        count=count+len(bytess)
        
        s.connect(addr)
        #fname=sys.argv[i]
        fname=filename#(fname.split('/'))[-1]
        #fname.encode('utf-8')
        sendNum=s.send(bytes(fname,'utf8'))
        name=s.recv(1024)
        #if not by:
        #       by=s.recv(2048)
        sendNum=0
        sendNum=sendNum+s.send(bytess)
        bytess=fi.read(65536)
        while bytess:
                count=count+len(bytess)
                sendNum=sendNum+s.send(bytess)
                bytess=fi.read(SND_SIZE)
        fi.close()
        print("the file length is: ",count,"bytes")
        print("send ",sendNum,"bytes data")      

        by=s.recv(RCV_BUF_SIZE)
        if name!=b'None':
                file=open(name.decode().split('/')[-1],'wb')
                file.write(by)
                file.close()
                print("get file: ",name.decode())
        ip,p=addr
        print("\t\t"+name.decode('utf8')+"\nget response from "+ip,':',p,'\n')
        #s.close()

       
if len(sys.argv)<2:
        filename=input("the filename to send (dir):\n")
        TCPsend(s,addr,filename)
else:
        for i in range(1,len(sys.argv)):
                filename=sys.argv[i]
                TCPsend(s,addr,filename)

##      s=socket.socket()
##      s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SND_BUF_SIZE)
##      s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RCV_BUF_SIZE)
s.close()

