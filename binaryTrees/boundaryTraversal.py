# https://takeuforward.org/data-structure/boundary-traversal-of-a-binary-tree/

# 1. travel extreme left and take non leaf nodes
# 2. take only leaf nodes from bottom to top (preorder/inorder)
# 3. travel extreme right and take non leaf ndoes and reverse it

left_travel = []
right_travel = []
leaf_travel = []

class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def leftTravel(self, node):
        curr = node.left
        while curr:
            if self.isLeaf(curr):
                break
            else:
                left_travel.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        return left_travel
    
    def righTravel(self, node):
        curr = node.right
        while curr:
            if self.isLeaf(curr):
                break
            else:
                right_travel.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
        right_travel.reverse()
    
    def leafTravel(self, node):
        if node == None:
            return
        if self.isLeaf(node):
            leaf_travel.append(node.val)
        self.leafTravel(node.left)
        self.leafTravel(node.right)

    def boundaryTraversal(self, root):
        if not root:
            return []
        ans = []
        ans.append(root.val)
        
        self.leftTravel(root)
        self.leafTravel(root)
        self.righTravel(root)

        ans.extend(left_travel)
        ans.extend(leaf_travel)
        ans.extend(right_travel)
        
        return ans
TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.left.left = Tree(5)
TreeNode.left.right = Tree(4)
TreeNode.left.right.right = Tree(11)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)

print(TreeNode.boundaryTraversal(TreeNode))

