import Queue

class IoService():
    def __init__(self,path):
        self.path = "./http/"+path

        self.q = Queue.Queue()

    def read(self):
        file = open(self.path,'r')
        lines = file.readlines()
        
        for line in lines:
            self.q.add(line)
        file.close()

        return "".join(self.q.queue)
