import threading
import random
import time


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        # Implement enqueue function
        while True:
            self.lock()
            if not ((self.tail + 1) % self.size == self.head):
                if (self.head == -1 and self.tail == -1):
                    self.head = 0
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                self.unlock()
                break
            self.unlock()
            time.sleep(1)

    def dequeue(self):
        # Implement dequeue function
        while True:
            self.lock()
            if not (self.head == -1 and self.tail == -1):
                element = self.queue[self.head]
                if (self.head == self.tail):
                    self.head = -1
                    self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self.unlock()
                return element
            self.unlock()
            time.sleep(1)


def producer():
    while True:
        # Implement producer function
        randNum = random.randint(1, 10)
        time.sleep(randNum)
        q.enqueue(randNum)


def consumer():
    while True:
        # Implement consumer function
        randNumber = random.randint(1, 10)
        time.sleep(randNumber)
        num = q.dequeue()
        if num is not None:
            print(num)


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
