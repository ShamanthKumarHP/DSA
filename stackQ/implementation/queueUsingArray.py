class Queue:
    def __init__(self, size):
        self.queue = [None for n in range(size)]
        self.__maxSize = size
        self.__first = -1
        self.__last = -1
        self.__cnt = 0

    def __isQfull(self):
        if self.__cnt + 1 > self.__maxSize:
            return True
        return False
    
    def __isQempty(self):
        if self.__cnt < 0:
            return True
        return False

    def pushQ(self, val):
        if not self.__isQfull():
            if self.__last == -1 and self.__first == -1:
                self.__first = 0
                self.__last = 0
                self.queue[self.__last ] = val
            else:
                self.__last = (self.__last + 1) % self.__maxSize
                self.queue[self.__last ] = val
            self.__cnt += 1
        else:
            print("Queue is full")
    
    def popQ(self):
        if not self.__isQempty():
            val = self.queue[self.__first]
            self.__first = (self.__first + 1) % self.__maxSize
            self.__cnt -= 1

            if self.__isQempty():
                self.__first = -1
                self.__last = -1
            print("popped", val)
    
    def peekQ(self):
        if not self.__isQempty():
            val = self.queue[self.__first % self.__maxSize]
            print("peeked", val)
    
    def sizeofQ(self):
        print('size', self.__cnt)
    
q = Queue(4)
q.pushQ(1)
q.pushQ(2)
q.pushQ(4)
q.pushQ(13)
q.pushQ(133)

q.popQ()
q.popQ()
q.popQ()

q.pushQ(11)
q.pushQ(1)
q.peekQ()