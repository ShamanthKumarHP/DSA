from TrieNode import Node

# naive N*N*logN
# N*N for all combination and logN for set
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        counter = 0
        for i in word:
            if not node.containsKey(i):
                counter += 1
                node.put(i)
            node = node.get(i)
    


        