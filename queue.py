from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def insert(self, value):
        self.queue.appendleft(value)

    def __str__(self):
        return str(self.queue)

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
        return self.queue.pop()

    def size(self):
        c = 0
        for i in self.queue:
            c += 1
        return c

    def first(self):
        return self.queue[-1]

    def is_empty(self):
        if self.size() == 0:
            return True
       

    

if __name__ == '__main__':
    pass
    #       using array:
    # queue = []
    # queue.insert(0,131.10)
    # queue.insert(0,132.12)
    # queue.insert(0,135.00)
    # queue.pop()
    # print(queue)
    #       using deque:
    # q = Queue()
    # q.insert(5)
    # q.insert(10)
    # q.insert("whoa")
    # q.pop()
    # q.insert(1)
    # print(q.is_empty())
    # print(q.size())
    # print(q)
