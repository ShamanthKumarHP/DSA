class Stack:
    def __init__(self, n) -> None:
        self.array = [ -1 for i in range(n)]
        self.top = -1

    def __isOverFlow(self):
        if self.top + 1 >= len(self.array):
            print("overflow")
            return True

    def __isUnderFlow(self):
        if self.top < 0 :
            print("underflow")
            return True
    
    def append(self, val):
        if not self.__isOverFlow():
            self.top += 1
            self.array[self.top] = val

    def pop(self):
        if not self.__isUnderFlow():
            val = self.array[self.top]
            self.top -= 1
            return val
    
    def sTop(self):
        if not self.__isUnderFlow() or not self.__isOverFlow():
            return self.array[self.top]
    
    def sSize(self):
        if not self.__isUnderFlow() or not self.__isOverFlow(): 
            return self.top+1
        

obj = Stack(4)
obj.pop()
obj.append(3)
obj.append(33)
obj.append(1)
print(obj.pop())
print(obj.pop())
print(obj.pop())


print("check overflow", obj._Stack__isOverFlow())
print(obj.sTop())
print(obj.sSize())
