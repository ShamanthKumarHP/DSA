`Note 1`
dp = [ [0] * cols] * rows # not good for 2d dp. Only 1 d is good. copy by reference it is
use below
dp2 =  [[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
    dp[i][0] = matrix[i][0]
    dp2[i][0] = matrix[i][0]

`Note 2`
strings
note for string[1:-1:-1] does not work, as it represent last index - middle value
dont fetch value of first element like this

`Note 3`
better to pass variables rather than keeping it as class variables

`Note 4`
Topo sort is strictly for DAG, do not apply for non acyclic graph to check if it has cycle
To check if it has cycle, better to check with Kahn's algo or DFS algo

undirected unit weight graph -> BFS
undirected positive weight graph -> Dijktra
DAG -> Toposort
DAG/DCG -> Dijktra


# Types of Binary Tree 
### Based on the number of children:
1. Full Binary Tree: 
    Every parent node/internal node has either 2 or no children.
2. Degenerate or pathological Binary Tree: 
    Only 1 child at each node. (LL)
3. Skewed Binary Tree. 
    Only 1 child but either dominated by the left nodes or the right nodes.


#### Based on the completion levels:
1. Complete Binary Tree: (Like I'm writing something on paper, and it is complete)
    All the levels are completely filled except possibly the last level 
    and the last level has all keys as left as possible.

2. Perfect Binary Tree: (Looks perfect)
    All the internal nodes have two children and 
    All leaf nodes are at the same level. 

3. Balanced Binary Tree: (Trying to balance)
    The difference between the height of the left and the right subtree for each node is either 0 or 1.

### Special Trees:
1. Binary Search Tree: 
    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.

2. AVL Tree:
    AVL tree is a self-balancing Binary Search Tree (BST) 

3. B Trees:
    Each node in a B-tree can have multiple child nodes and multiple keys, and the keys are used to index and locate data items.

4. B+ Trees:
    B+ tree, all data items are stored in the leaf nodes, while the internal nodes only contain keys for indexing and locating the data items. 

5. Segment Trees(statistic tree):
    A tree data structure used for storing information about intervals, or segments.
    It’s a structure that cannot be modified once it’s built.

