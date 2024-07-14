# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # provided current node's value should be greater than largest value of left subtree
    # and lesser than smallest value of right subtree
    # idea is to perform post order ie go left, right and then root

    def postOrder(self, root):
        if not root:
            # pass extreme high value as minimum and extreme high value as maximum
            return (0, float('inf'), float('-inf'))
        
        (left_bst_size, left_min, left_max) = self.postOrder(root.left)
        (right_bst_size, right_min, right_max) = self.postOrder(root.right)

        # case 1: both side are valid
        if root.val > left_max and root.val < right_min:
            # in case of leaf nodes, we need to take especially take min(left_min, root.val) , max(root.val, right_max)
            return (1 + left_bst_size + right_bst_size, min(left_min, root.val) , max(root.val, right_max))

        # case 2: any one of them is valid
        # pass extreme high value as minimum and extreme high value as maximum
        return (max(left_bst_size, right_bst_size), float('inf'), float('-inf'))

    def largestBST(self, root) -> None:
        bst, _, _ = self.postOrder(root)
        return bst


def to_binary_tree(items):
    if not items:
        return None
    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root

lst = [6,2,2,None,2,1,3]
root = to_binary_tree(lst)
ob = Solution()
print(ob.largestBST(root))

    
    
        