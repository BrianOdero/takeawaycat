import socket

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 4456
    
    
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    while True:
    
    
        multicastgroup = '224.1.1.1'
        client.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,2)

        data = "hello Brian"

        client.sendto(data.encode(),(multicastgroup,4455))

        data,addr = client.recvfrom(1024)
        print(f"received : {data}")

    
    
    
    

