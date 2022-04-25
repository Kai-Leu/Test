import socket
import select
import redis
import time
import threading

print_lock = threading.Lock()

r = redis.Redis()

sockets = []
host = "127.0.0.1"

#SendFunction
def sendsh(message,port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.sendto(message,(host,port))
    server_socket.close()


##Receive
for port in range(1600,1650):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host,port))
    sockets.append(server_socket)

empty = []


def read():
    while True:
        with print_lock:
            readable, writeable, exceptional  = select.select(sockets, empty, empty,0.1)
            for s in readable:
                (data, addr) = s.recvfrom(1024)
                data = data.decode("utf-8")
                host,port = addr
                r.set(port,data)
                #print("Received:", data, port)

            

def write():
    while True:
        with print_lock:
            keys = r.keys("17*")
            for i in keys:
                message = r.get(i)
                port = int(i)
                sendsh(message,port)
                #print("Send",message,port)
            time.sleep(0.3)    
            
        
def main():
    t1 = threading.Thread(target=write)
    t2 = threading.Thread(target=read)
    print("Connected")
    t1.start()
    t2.start()

if __name__  == "__main__":
    main()



    #Test Aenderung Filipe Ineichen