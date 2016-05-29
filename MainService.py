import socket, time, threading, ClientService

class MainService(threading.Thread):
    def __init__(self, host, port):
        super(MainService, self).__init__()

        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host,port))
        self.sock.listen(1)

        print ("host ",host," port ",port)
        
    def run(self):
        client_number = 0
        while 1:
            connection, address = self.sock.accept()
            client = ClientService.ClientService(self.sock, connection, address, client_number)
            client.start()
            client_number += 1

proc = MainService("127.0.0.1",80)
proc.start()
