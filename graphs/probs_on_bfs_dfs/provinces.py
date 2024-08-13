class Solution:
    def dfs(self, node, visited, adj_list):
            visited[node] = 1
            # ans.append(node)
            adj_nodes = adj_list[node]
            for ele in adj_nodes:
                if not visited.get(ele, None):  
                    self.dfs(ele, visited, adj_list)
            return
    
    def findCircleNum(self, isConnected) -> int:
        # create a adjacency list
        r = len(isConnected) 
        adj_list = [[] for _ in range(r)]
        for i in range(r):
            for j in range(r):
                if i!=j and isConnected[i][j] == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        print(adj_list)
        cnt = 0
        visited = dict()
        for i in range(r):
             if not visited.get(i, None):
                  cnt = cnt + 1
                  self.dfs(i, visited, adj_list)
       
        return cnt

ob = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(ob.findCircleNum(isConnected))