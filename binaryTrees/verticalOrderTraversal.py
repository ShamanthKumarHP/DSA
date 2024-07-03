from collections import deque, defaultdict
class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def vertical(self, root):
        # (x, y)
        virtus = defaultdict(lambda: defaultdict(lambda: list()))
        q = []
        q.append((root, (0, 0)))
        while q:
            node, (x, y) = q.pop(0)

            virtus[x][y].append(node.val)
            
            # virtus.update({(x,y): node[0].val})
            if node.left:
                q.append((node.left, (x-1,y+1)))
            if node.right:
                q.append((node.right, (x+1,y+1)))

        ans = []
        for values in sorted(virtus.items()):
            col = []
            y_vals = virtus[values[0]]
            for y, vals in y_vals.items():
                col.extend(sorted(vals))
            ans.append(col)
        return ans
        
TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.right = Tree(4)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)

ans = TreeNode.vertical(TreeNode)
def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()
printResult(ans)


a = defaultdict(list)
b = defaultdict(lambda: defaultdict(set))
# nodes = defaultdict(lambda: list())
# print(nodes)
# nodes[1].append(3)
# nodes[1].append(1)
# # nodes[1] = 2
# print(nodes)

# # nodes.setdefault(1, []).add(3)
# # print(nodes)
# # nodes.setdefault(1, []).append(3)
# # print(nodes)

# # print(TreeNode.vertical(TreeNode))
# print()
# d = defaultdict(lambda: 2)
# # Add some data to the nested defaultdict
# print(d[1])
# nodes['A'].add(1)
# nodes['A'].add(2)
# nodes['B'].add(3)
# # print(nodes)


# d = defaultdict(lambda: defaultdict(lambda: set()))


