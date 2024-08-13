class Solution:
    def dfs(self, i, color, graph, visited):
        visited[i] = color
        for j in graph[i]:
            if visited[j] == -1:
                if self.dfs(j,  not color, graph, visited) == False:
                    return False
            elif visited[j] == color:
                return False
        return True

    def isBipartite(self, graph) -> bool:
        n = len(graph)
        visited = [-1 for _ in range(n)]
        for i in range(n):
            if visited[i] == -1:
                ret = self.dfs(i, 0, graph, visited)
                if ret == False:
                    return False
        return True

obj = Solution()
graph = [[1,3],[0,2],[1,3],[0,2]]
print(obj.isBipartite(graph))

        
