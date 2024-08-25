# https://www.youtube.com/watch?v=E6DeC0Zpdns codestoryMIK
# find strongly connected components
# step 1 : sort edges as per their finishing time (like toposort, but not exactly)
# step 2 : reverse the edges
# step 3 : find scc . number of dfs calls

# applicable for directed graph; a node can reach all other nodes

class SCC:
    def dfs(self, node, visited, stack, adj_list):
        visited[node] = 1
        for it in adj_list[node]:
            if visited[it] == 0:
                self.dfs(it, visited, stack, adj_list)
        stack.append(node)

    def dfs_after_rev(self, node, visited, adj_list, sccs):
        visited[node] = 1
        for it in adj_list[node]:
            if visited[it] == 0:
                self.dfs_after_rev(it, visited, adj_list, sccs)
        sccs.append(node)
    
    def kosaraju(self, n, adj_list):
        stack = []
        visited = [0 for i in range(n)]

        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, visited, stack, adj_list)

        rev_adj_list = [[] for i in range(n)]
        for idx, adjs in enumerate(adj_list):
            for it in adjs:
                rev_adj_list[it].append(idx)
        
        visited = [0 for i in range(n)]
        cnt_scc = 0
        ans = []
        while stack:
            node = stack.pop()
            if visited[node] == 0:
                cnt_scc += 1
                scss = []
                self.dfs_after_rev(node, visited, rev_adj_list, scss)
                ans.append(scss)

        return ans, cnt_scc



obj = SCC()
edges = [[1, 0], [0, 2],
        [2, 1], [0, 3],
        [3, 4]]
n = 5
adj_list = [ [] for i in range(n)]

for x,y in edges:
    adj_list[x].append(y)


print(obj.kosaraju(n, adj_list))