# Problem Statement: You are given an n, m which means the row and column of the 2D matrix, 
# and an array of size k 
# denoting the number of operations. Matrix elements are 0 if there is water or 
# 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in 
# the matrix. The array has k operator(s) and each operator has two integers 
# A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] 
# from sea to island. Return how many islands are there in the matrix after each operation. 
# You need to return an array of size k.

#  TC = 4*alpha => constant
class Disjoint:
    def __init__(self, V) -> None:
        self.rank = [0 for i in range(V+1)] # just to support 1 base indexing
        self.parent = [i for i in range(V+1)]

    def getUltimateParent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.getUltimateParent(self.parent[u])
        return self.parent[u]

    def unionByRank(self,x,y):
        x_up = self.getUltimateParent(x)
        y_up = self.getUltimateParent(y)

        # both belong to same component already
        if x_up == y_up:
            return
        
        if self.rank[x_up] < self.rank[y_up]:
            self.parent[x_up] = y_up
        elif self.rank[x_up] > self.rank[y_up]:
            self.parent[y_up] = x_up
        else: # same rank
            self.parent[y_up] = x_up
            self.rank[x_up] = self.rank[x_up] + 1

def findNumIslands(matrix, operators):
    rows = len(matrix)
    cols = len(matrix[0])
    ds = Disjoint(cols*rows)

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    visited = [[0 for i in range(cols)] for j in range(rows)]

    cnt = 0
    ans = []
    for x,y in operators:
        if x == 1 and y==2:
            pass
        if visited[x][y] != 0:
            # already visited
            ans.append(cnt)
            continue
        cnt = cnt + 1
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            currNode = x*cols+y
            adjNode = nx*cols+ny
            if visited[nx][ny] == 1 and ds.getUltimateParent(adjNode) != ds.getUltimateParent(currNode):
                cnt = cnt - 1
                ds.unionByRank(currNode, adjNode)
        ans.append(cnt)
    return ans


operators = [[0, 0], [0, 0], [1, 1], [1, 0], [0, 1],
[0, 3], [1, 3], [0, 4], [3, 2], [2, 2], [1, 2], [0, 2]]
m = 4
n = 5
matrix = [[0 for i in range(n)] for j in range(m)]
print(findNumIslands(matrix, operators))



