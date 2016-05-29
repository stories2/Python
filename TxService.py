import socket

class TxService():
    def __init__(self, sock, connection, address):
        self.sock = sock
        self.connection = connection
        self.address = address

    def send(self, string):
        print ("send msg ",string)
        self.connection.send(str.encode(string))
        #self.connection.close()
