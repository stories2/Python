#-*- coding: utf-8 -*-
import socket

def release(connection):
    print ("shutdown http server")
    if(connection != None):
        connection.close()

def client_accepter(sock):
    client_num = 0
    connection = None
    #while 1:
    connection, address = sock.accept()
    print ("client #",client_num," start")
    client_num += 1
    client_room(sock, connection, address)

    release(connection)

def comp(origin, target):
    i = 0
    str_length = len(origin)
    for i in range(str_length):
        if(origin[i] != target[i]):
            return 0
    return 1

def client_room(sock, connection, address):

    pattern = ['\r','\n','\r','\n']
    buffer = ['','','','']
    respone_str = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<body>It Works!<body>"
    i = 0
    str_length = len(buffer);
    print ("================HTTP REQUEST================\n")
    while 1:
        for i in range(1, str_length):
            buffer[i-1] = buffer[i]
        buffer[str_length - 1] = connection.recv(1)
        buffer[str_length - 1] = buffer[str_length - 1].decode("ascii")
        print (buffer[str_length - 1],end = '')
        if(comp(buffer,pattern)):
            print ("================HTTP RESPONSE================\n",respone_str)
            connection.send(str.encode(respone_str))
            break
        

host = "127.0.0.1"
port = 80
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)
print ("start listening")

client_accepter(sock)
