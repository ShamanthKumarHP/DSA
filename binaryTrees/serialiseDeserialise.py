class Tree():
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        serial = ""
        q = []
        q.append(root)

        while q:
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                if node:
                    serial = serial + str(node.val) + ","
                    q.append(node.left)
                    q.append(node.right)
                else:
                    serial += "#,"
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        
        data = data.split(",")
        pq = []

        root = TreeNode(int(data.pop(0)))
        pq.append(root)

        while pq:
            node = pq.pop(0)

            curr = data.pop(0)
            if curr != "#":
                node.left = TreeNode(int(curr))
                pq.append(node.left)

            curr = data.pop(0)
            if curr != "#":
                node.right = TreeNode(int(curr))
                pq.append(node.right)
            
        return root

    
def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)

    root = Tree(next(it))
    q = [root]
    
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = Tree(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = Tree(val)
            q.append(node.right)
    return root

lst = [1,2,3,None,None,4,5]
root = to_binary_tree(lst)



# OR
TreeNode = Tree()
print(TreeNode.serialize(root))


s = "a,b,c,"
print(s.split(','))