import socket, threading, Queue

class RxService(threading.Thread):
    def __init__(self, sock, connection, super_q):
        super(RxService, self).__init__()

        self.sock = sock
        self.connection = connection
        self.super_q = super_q

        self.pattern = ['\r','\n','\r','\n']
        self.buffer = ['','','','']
        self.q = Queue.Queue()
        
    def run(self):
        while 1:
            data = self.connection.recv(1).decode("ascii")
            #print (data,end="")
            
            i = 0
            str_length = len(self.buffer)

            for i in range(1, str_length):
                self.buffer[i - 1] = self.buffer[i]
            self.buffer[str_length - 1] = data
            
            same = 1
            for i in range(str_length):
                if(self.pattern[i] != self.buffer[i]):
                    same = 0
                    break
            if(same == 1):
                print ("ok")
                self.super_q.queue.append("".join(self.q.queue))
                self.super_q.rear += 1
                self.q = Queue.Queue()
            else:
                self.q.add(data)
