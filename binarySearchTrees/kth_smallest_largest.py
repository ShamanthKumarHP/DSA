class Tree():
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
    
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


# OR
# TreeNode = Tree(1)
# TreeNode.left = Tree(2)
# TreeNode.right = Tree(10)
# TreeNode.left.left = Tree(3)
# TreeNode.left.right = Tree(4)
# TreeNode.right.left = Tree(13)
# TreeNode.right.right = Tree(14)

class Solution:
    def in_order_recursion(self, root, cnt, k, ans):
        if not root or cnt[0]>=k:
            return
        
        self.in_order_recursion(root.left, cnt, k, ans)

        cnt[0] = cnt[0] + 1
        if cnt[0] == k:
            ans[0] = root.val
            return
        
        self.in_order_recursion(root.right, cnt, k, ans)

    def kthSmallest(self, root, k: int) -> int:
        # in order traversal
        if not root:
            return root
        cnt = [0]
        ans = [float('inf')]
        self.in_order_recursion(root, cnt, k, ans)
        return ans[0]
    
    def large_in_order_recursion(self, root, cnt, k, ans):
        if not root or cnt[0]>=k:
            return
        
        self.large_in_order_recursion(root.right, cnt, k, ans)

        cnt[0] = cnt[0] + 1
        if cnt[0] == k:
            ans[0] = root.val
            return

        self.large_in_order_recursion(root.left, cnt, k, ans)
        

    def kthLargest(self, root, k: int) -> int:
        # in order traversal
        if not root:
            return root
        cnt = [0]
        ans = [float('inf')]
        self.large_in_order_recursion(root, cnt, k, ans)
        return ans[0]

    def morris_smallest(self, node,k):
        cnt = 0
        while node:
            if not node.left:
                cnt = cnt + 1
                if cnt == k:
                    return node.val
                node = node.right
            else:
                prev = node.left
                while prev.right and prev.right != node:
                    prev = prev.right
                if not prev.right:
                    prev.right = node
                    node = node.left
                elif prev.right == node:
                    cnt = cnt + 1
                    if cnt == k:
                        return node.val
                    prev.right = None
                    node = node.right
        return 0
    
    def morris_largest(self, node,k):
        cnt = 0
        while node:
            if not node.right:
                cnt = cnt + 1
                if cnt == k:
                    return node.val
                node = node.left
            else:
                prev = node.right
                while prev.left and prev.left != node:
                    prev = prev.left
                if not prev.left:
                    prev.left = node
                    node = node.right
                elif prev.left == node:
                    cnt = cnt + 1
                    if cnt == k:
                        return node.val
                    prev.left = None
                    node = node.left
        return 0

lst = [4,2,5,None,3]
root = to_binary_tree(lst)

ob = Solution()
print(ob.kthSmallest(root, 1))
print(ob.morris_smallest(root, 1))

print(ob.kthLargest(root, 2))
print(ob.morris_largest(root, 2))
