# stack (val, count)

class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def pip(self, root):
        stack = []

        preOrder = [] #1
        inOrder = [] #2
        postOrder = [] #3

        stack.append((root,1))
        while stack:
            node, cnt = stack.pop()
            #PreOrder
            if cnt == 1:
                preOrder.append(node.val)
                cnt = cnt + 1
                stack.append((node, cnt))

                if node.left:
                    stack.append((node.left, 1))
            
            elif cnt == 2:
                inOrder.append(node.val)
                cnt = cnt + 1
                stack.append((node, cnt))

                if node.right:
                    stack.append((node.right, 1))
                
            elif cnt == 3:
                postOrder.append(node.val)

        return preOrder, inOrder, postOrder
    
    
TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.right = Tree(3)
TreeNode.left.left = Tree(4)
TreeNode.left.right = Tree(5)
TreeNode.right.left = Tree(6)


print(TreeNode.pip(TreeNode))
