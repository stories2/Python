import socket, time, threading, RxService, TxService, Queue, IoService

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

                io = IoService.IoService("index.html")
                src = io.read()
                length = len(src)
                msg = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "+str(length)+"\r\n\r\n"+src
                self.tx.send(msg)
                break
