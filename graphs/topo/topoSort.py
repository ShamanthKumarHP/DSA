# works only for DAG
class Solution:
    def dfs(self, node, visited, adj_list, stack):
        visited[node] = 1
        for i in adj_list[node]:
            if visited[i] == 0:
                self.dfs(i, visited, adj_list, stack)
        stack.append(node)
        return
    
    def topoSort(self, n, adj_list):
        visited = [0 for i in range(n)]
        stack = []
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, visited, adj_list, stack)
        
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans

obj = Solution()
adj_list = [[1],[2],[0]]
n = 3
print(obj.topoSort(n, adj_list))