# A string is called a complete string if every prefix of this string is also present in the array ‘A’. 
# Ninja is challenged to find the longest complete string in the array ‘A’.
# If there are multiple strings with the same length, return the lexicographically smallest one 
# and if no string exists, return "None".

from TrieNode import Node

# class PrefixNode (Node):
#     def checkIfPrefixExists(self, word):
#         node = self.root
#         for i in word:
#             if self

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for i in word:
            if not node.containsKey(i):
                node.put(i)
            node = node.get(i)
        node.setEnd()
    
    def checkIfPrefixExists(self, word):
        # to check if all prefix exists
        node = self.root
        for i in word:
            node = node.get(i)
            if node.isEnd(i):
                continue
            else:
                return False
        return True 

    def longestStringWithAllPrefix(self, words):
        # traverse though all words and insert first
        for word in words:
            self.insert(word)
        
        # traverse again and see if all prefix exists for the same
        ans = ""
        for word in words:
            if self.checkIfPrefixExists(word):
                if len(ans) > len(word):
                    continue
                elif len(ans) < len(word):
                    ans = word
                else:
                    ans = word if word > ans else ans
        
        return ans
                    
            
        
            


        
