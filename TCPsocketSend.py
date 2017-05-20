#coding=utf-8
import sys
import socket
print(sys.argv[0],len(sys.argv))



SND_BUF_SIZE=1024*1024
RCV_BUF_SIZE=1024*1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='139.199.189.194'#'222.20.94.67'#102
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
        bytess=fi.read()
        fi.close()
        print("the file length is: ",len(bytess),"bytes")
        s.connect(addr)
        #fname=sys.argv[i]
        fname=filename.split('/')[-1]
        #fname.encode('utf-8')
        sendNum=s.send(bytes(fname,'utf8'))
        name=s.recv(1024)
        #if not by:
        #       by=s.recv(2048)
        sendNum=s.send(bytess)
        print("send ",sendNum,"bytes data")
        
        by=s.recv(RCV_BUF_SIZE)
        if name!=b"None":
                file=open(name.decode().split('/')[-1],'wb')
                file.write(by)
                file.close()
                print("get file: ",name.decode())
        ip,p=addr
        print("\t\t"+name.decode('utf8')+"\nget response from "+ip,':',p,'\n')
        s.close()
if len(sys.argv)<2:
        filename=input("the filename to send (dir)：\n")
        while filename:
                TCPsend(s,addr,filename)
                filename=input("the filename to send (dir):\n")
                s=socket.socket()
                s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SND_BUF_SIZE)
                s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RCV_BUF_SIZE)
else:
        for i in range(1,len(sys.argv)):
                filename=sys.argv[i]
                TCPsend(s,addr,filename)
                s=socket.socket()
                s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SND_BUF_SIZE)
                s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RCV_BUF_SIZE)


s.close()
                
