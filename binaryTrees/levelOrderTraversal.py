                            
from collections import deque

# TreeNode class represents
# a node in a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        # Create a list to store levels
        ans = []
        if not root:
            # If the tree is empty,
            # return an empty list
            return ans

        # Create a queue to store nodes
        # for level-order traversal
        q = deque()
        # Enqueue the root node
        q.append(root)

        while q:
            # Get the size of the current level
            size = len(q)
            # Create a list to store
            # nodes at the current level
            level = []

            for i in range(size):
                # Get the front node in the queue
                node = q.popleft()
                # Store the node value
                # in the current level list
                level.append(node.val)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Store the current level
            # in the answer list
            ans.append(level)
        # Return the level-order
        # traversal of the tree
        return ans

# Function to print
# the elements of a list
def printList(lst):
    # Iterate through the
    # list and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance
    # of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    # Printing the level order traversal result
    for level in result:
        printList(level)
                           
                        