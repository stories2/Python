class Queue():
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = -1

    def is_empty(self):
        return self.front + 1 > self.rear

    def add(self, string):
        self.queue.append(string)
        self.rear += 1

    def delete(self):
        if(self.is_empty()):
            return 0
        self.front += 1
        return self.queue[self.front]
