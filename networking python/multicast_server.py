import socket

if __name__=="__main__":
    host = '127.0.0.1'
    port = 4456
    multicastgroup = '224.1.1.1'
    
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((host,port))
    
    
    server.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,socket.inet_aton(multicastgroup) + socket.inet_aton('0.0.0.0'))
    
    print("waiting for message")
    
    while True:
        data,addr=server.recvfrom(1024)
        print("received : {data}")
