import threading

class thread_test(threading.Thread):
    def __init__(self,string):
        super(thread_test,self).__init__()
        self.string = string
    def run(self):
        print (self.string)

th = thread_test("hello")
th.start()
