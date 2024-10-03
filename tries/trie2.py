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
    

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if not node.containsKey(i):
                node.put(i)
            node = node.get(i)
            node.increaseCount()
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if node.containsKey(i):
                node = node.get(i)
            else:
                return False
        if node.isEnd():
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if not node.containsKey(i):
                return False
            node = node.get(i)
        return True
        
    
    def eraseWord(self, word):
        node = self.root
        for i in word:
            if node.containsKey(i):
                node = node.get(i)
                node.decreasePrefix()
        node.deleteWord()
    
    def countWordsEqualTo(self, word):
        node = self.root
        for i in word:
            if not node.containsKey(i):
                return 0
            node = node.get(i)
        return node.prefix
    
    def countWordsStartingWith(self, prefix):
        node = self.root
        for i in prefix:
            if node.containsKey(i):
                node = node.get(i)
        return node.prefix




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)