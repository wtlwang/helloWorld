#coding=utf8
import sys
def TCPsocketGet():
    import socket

    #socket.setdefaulttimeout(2.0)
    RCVBUF_SIZE=1024*1024
    RCV_SIZE=65536
    s=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)#TCP
    defBuffer=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    defBufferRecv=s.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    #defBuf=s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUFORCE,1024*1024)
    print("the defalut send buffer size is :",defBuffer)
    print('the defalut receive buffer size is :',defBufferRecv)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RCVBUF_SIZE)
    defBufferRecv=s.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    print("the receive buffer size now is :",defBufferRecv)

    host=''
    port=8083
    s.bind((host,port))
    s.listen(5)
    TIME_OUT=10#0.0001 #(sec)
    while(1):
        c,addr=s.accept()

        print('Got connection from',addr)
        by=c.recv(1024)
        print(by.decode())
        if len(sys.argv)<2:
            c.send(b'None')
            
        else:
            c.send(bytes(sys.argv[1],'utf-8'))
        fname=by.decode('utf8').rpartition('\\')[-1]
        fname=fname.split('/')[-1]
        f=open(fname,'wb')
        count=0
        data=c.recv(65536)
        count=count+len(data)
        c.settimeout(TIME_OUT)
        #data2=b'1'
        while 1:
            try:
                f.write(data)
                f.flush()
                data=c.recv(RCV_SIZE)
                count=count+len(data)
                #data=data+data2
                
            except socket.timeout:
                break
        f.close()       
        if len(sys.argv)<2:
            c.send(b'Got the file: '+by+b' size(bytes) is: '+bytes(str(count),'utf8'))
        else:
            fin=open(sys.argv[1],'rb')
            c.send(fin.read())
            fin.close()
        c.close()


        
        #f.flush()
    
    ##    if data2:
    ##        f=open(fname,'ab')
    ##        f.write(data2)
    ##        f.close()
    ##        print("receive ",len(data2),"at the second time")
        print("receive ",count,"bytes data at all(total)")

        print('Get the file: "'+fname+'"','is saved in current dir')
       
       
        
    s.close()
if __name__=="__main__":
    TCPsocketGet()

