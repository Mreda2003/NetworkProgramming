from socket import *

s = socket(AF_INET , SOCK_STREAM)
host = '127.0.0.1'
port = 40674
s.bind((host , port))
s.listen(5)
print("socket is listening")
c , addr = s.accept()
c.send("Get connectin from " , addr)
c.close()