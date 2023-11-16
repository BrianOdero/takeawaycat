import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    
    
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    server.bind((host,port))
    
    while True:
        data,address = server.recvfrom(1024)
        data = data.decode("utf-8")
        
        print(f"Client : {data}" )
        data = data.upper()
        data = data.encode() 
        server.sendto(data,address)