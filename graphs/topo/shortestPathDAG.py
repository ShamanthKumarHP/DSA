# could have also be done using Dijkstra (acylic+cyclic)
# but if it is DAG, it is better to do with toposort (acyclic)

class Solution:
    def dfs(self, node, adj_list, visited, stack):
        visited[node] = 1
        for i, wt in adj_list[node]:
            if visited[i] == 0:
                self.dfs(i, adj_list, visited, stack)
        stack.append(node)
        return

    def topoSort(self, n, adj_list):
        # we can keep stack as it is. to avoid extra space
        stack = []
        visited = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, adj_list, visited, stack)
        
        return stack

    def findMinPath(self, src, adj_list):
        n = len(adj_list)
        topo = self.topoSort(n, adj_list)

        dist = [1e9 for i in range(n)]
    
        # mark source element distance as 0
        dist[src] = 0

        # now take elements from stack and free to adjacent nodes
        while topo:
            # pop until u get src node.
            # before elements, obviously we cannot travel
            if topo[-1] != src:
                topo.pop()
                continue
            
            node = topo.pop()
            for adj_node , adj_dist in adj_list[node]:
                if (dist[node] + adj_dist < dist[adj_node]):
                    dist[adj_node] = dist[node] + adj_dist
        
        for i in range(n):
            if dist[i] == 1e9:
                dist[i] = -1
            
        return dist

abc = Solution()
n = 4
adj_list = [[] for i in range(n)]
edge = [[0,1,2],[0,2,1]]
for u,v,w in edge:
    adj_list[u].append((v, w))

src = 0

print(abc.findMinPath(src, adj_list))