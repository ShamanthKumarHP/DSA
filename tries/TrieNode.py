class Node:
    def __init__(self):
        self.links = [None for i in range(26)]
        self.endswith = 0
        self.prefix = 0
    
    def containsKey(self, ch):
        return True if self.links[ord(ch) - ord('a')] else False
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch):
        self.prefix += 1
        self.links[ord(ch) - ord('a')] = Node()
    
    def isEnd(self):
        return True if self.endswith else False

    def setEnd(self):
        self.endswith += 1

    def increasePrefix(self):
        self.prefix += 1

    def decreasePrefix(self):
        self.prefix -= 1
    
    def deleteWord(self):
        self.endswith -= 1
