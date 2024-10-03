class Node:
    def __init__(self):
        self.links = [None, None] # Zero, One bit
    
    def get(self, bit):
        return self.links[bit]
    
    def put(self, bit):
        self.links[bit] = Node()
    
    def containsKey(self, bit):
        return True if self.links[bit] else False
    

class Trie:
    def __init__(self):
        self.root = Node()
    
    # def convert2binary(self, num):
    #     binary_val = bin(num).replace("0b", "")
    #     binary_val = binary_val.zfill(31)
    #     return binary_val

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            # check if that bit is set or not
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit)
            node = node.get(bit)
    
    def getMax(self, num):
        # binary_val = self.convert2binary(num)
        # if it 0 we will look for 1, vice versa
        node = self.root
        maxi = 0
        for i in range(31, -1, -1):
            # check if that bit is set, then check if opp bit is set
            bit = (num >> i) & 1
            if node.containsKey(1 - bit):
                maxi = maxi | (1 << i)
                node = node.get(1-bit)
            else:
                node = node.get(bit)
        
        return maxi

class Solution:
    def findMaximumXOR(self, nums) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)

        maxi = 0
        for num in nums:
            maxi = max(maxi, trie.getMax(num))

        return maxi

        

obj = Solution()
nums = [3,10,5,25,2,8]
print(obj.findMaximumXOR(nums))