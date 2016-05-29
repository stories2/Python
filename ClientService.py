import socket, time, threading, RxService, TxService, Queue

class ClientService(threading.Thread):
    def __init__(self, sock, connection, address, client_num):
        super(ClientService, self).__init__()
        
        print ("Client #",client_num," addr ",address)

        self.q = Queue.Queue()
        self.sock = sock
        self.connection = connection
        self.address = address
        self.client_num = client_num
        
        self.rx = RxService.RxService(self.sock, self.connection, self.q)
        self.rx.start()

        self.tx = TxService.TxService(self.sock, self.connection, self.address)

    def run(self):
        while 1:
            if(self.q.is_empty() == False):
                print (self.q.delete())
                self.tx.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<body>It Works!<body>")
                break
