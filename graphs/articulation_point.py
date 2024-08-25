# https://www.youtube.com/watch?v=jFZsDDB0-vo
class Solution:
    def dfs(self, node, parent, tin, low, visited, adj_list, mark):
        visited[node] = 1
        tin[node] = self.timer
        low[node] = self.timer
        self.timer += 1
        child = 0
        for adjNode in adj_list[node]:
            if adjNode == parent:
                continue
            if visited[adjNode] == 0:
                self.dfs(adjNode, node, tin, low, visited, adj_list, mark)
                low[node] = min(low[node], low[adjNode])
                if low[adjNode] >= tin[node] and parent != -1: # child can have same value as node, so consider >= 
                  #node is articulation point
                  mark[node] = 1
                child = child + 1
            elif visited[adjNode] == 1:
                low[node] = min(low[node], tin[adjNode])
            
        if parent == -1 and child > 1:
            mark[node] = 1
        return

    def articulationPoint(self, n, adj_list):
        visited = [0 for i in range(n)]
        self.timer = 1
        tin = [0 for i in range(n)]
        low = [0 for i in range(n)]
        mark = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, -1, tin, low, visited, adj_list, mark)
        
        ans = []
        for i in range(n):
            if mark[i] == 1:
                ans.append(i)
        return ans