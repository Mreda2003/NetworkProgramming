from socket import *
from time import *
try: 
    s=socket(AF_INET, SOCK_STREAM)
    host="127.0.0.1"
    port=7002
    s.bind((host,port))
    s.listen(3)
    client, addr=s.accept()
    print("connection from ", addr[0])
    while True:
     x=client.recv(2048)
     print("client : ",x.decode('utf-8') , ctime())
     y=input(" server : ")
     client.send(y.encode('utf-8'))
    client.close()
except error as e:
 print(e)