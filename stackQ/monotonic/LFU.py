class DLL:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:
    
    def __init__(self, capacity: int):
        self.dict_map = {}
        self.max_capacity = capacity

        self.head = DLL(-1,-1)
        self.tail = DLL(-1,-1)
        self.tail.left = self.head
        self.head.right = self.tail

    def add_node(self, node):
        temp = self.head.right
        self.head.right = node
        node.left = self.head
        node.right = temp
        temp.left = node
    
    def remove_node(self, node):
        # have to remove node(least used will be at tail)
        prevNode = node.left
        nextNode = node.right
        prevNode.right = nextNode
        nextNode.left = prevNode

    def get(self, key: int) -> int:
        # get it at first
        if not self.dict_map.get(key, None):
            return -1
        node = self.dict_map[key]
        ans = node.val
        self.remove_node(node)
        self.add_node(node)
        return ans
    
    def put(self, key: int, value: int) -> None:
        if self.dict_map.get(key):
            node = self.dict_map[key]
            node.val = value
            self.remove_node(node)
            self.add_node(node)
        else:
            if len(self.dict_map) == self.max_capacity:
                del self.dict_map[self.tail.left.key]
                self.remove_node(self.tail.left)
            node = DLL(key,value)
            self.add_node(node) # put the node at first in DLL, right after dummy head
            self.dict_map[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

d = dict()
d