class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    # root, left, right
    
    def preOrder_recursion(self, root):
        ans = []
        def recursion(node):
            if node == None:
                return
            ans.append(node.val)
            recursion(node.left)
            recursion(node.right)
        recursion(root)
        return ans
    
    def preOrder_iterative(self, root):
        if root == None:
            return []
        
        stack = []
        stack.append(root)
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        return ans
    
    # left, root, right
    def inOrder_recursion(self, root):
        ans = []
        def recursion(node):
            if node == None:
                return
            recursion(node.left)
            ans.append(node.val)
            recursion(node.right)
        recursion(root)
        return ans
    
    # left, root, right
    def inOrder_iterative(self, root):
        if root == None:
            return
        ans = []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans

    
    # level order
    def levelOrder_iterative(self, root):
        #FIFO
        if root == None:
            return []
        q = []
        ans = []
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans


    #left, right, root
    def postOrder_recursion(self, root):
        if root is None:
            return []
        ans = []
        def recursion(node):
            if node is None:
                return
            recursion(node.left)
            recursion(node.right)
            ans.append(node.val)
        recursion(root)
        return ans

    # left, right, root
    # two stack or 1 stack 1 list (reverse)
    def postOrder_iterative_2_stack(self, root):
        if not root:
            return
        stack1 = []
        stack2 = []
        ans = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            stack2.append(node) # list append

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            
        while stack2: # list.reverse
            ans.append(stack2.pop().val)
        return ans

    def postOrder_iterative_1_stack(self, root):
        if not root:
            return
        curr = root
        temp = None
        stack = []
        ans = []
        while stack or curr:
            # to go complete left
            if curr != None:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1]
                if temp.right == None:
                    temp = stack.pop()
                    ans.append(temp.val)
                    # to comeback from complete right
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        ans.append(temp.val)
                else:
                    curr = temp.right
        return ans

TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.right = Tree(3)
TreeNode.left.left = Tree(4)
TreeNode.left.right = Tree(5)
TreeNode.right.left = Tree(6)


print(TreeNode.preOrder_recursion(TreeNode))
print(TreeNode.preOrder_iterative(TreeNode))
print()
print(TreeNode.inOrder_recursion(TreeNode))
print(TreeNode.inOrder_iterative(TreeNode))
print()
print(TreeNode.postOrder_recursion(TreeNode))
print(TreeNode.postOrder_iterative_2_stack(TreeNode))
print(TreeNode.postOrder_iterative_1_stack(TreeNode))
print()
print(TreeNode.levelOrder(TreeNode))
print()