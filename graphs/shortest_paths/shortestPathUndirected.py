# weighted graph
# level order traversal
# calc neighbours distance

class Solution:
    def bfs(self, source, adj_list):
        ans = [None for i in range(len(adj_list))]
        q = []
        ans[source] = 0
        q.append((source, 0))
        while q:
            node, dist = q.pop(0)
            for j in adj_list[node]:
                if ans[j] == None:
                    ans[j] = dist + 1
                    q.append((j,dist+1))
        
        return ans

obj = Solution()
edges = [[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
n = 9
adj_list = [[] for i in range(n)]
for src, dest in edges:
    adj_list[src].append(dest)

graph = []
source = 0
print(obj.bfs(source, adj_list))