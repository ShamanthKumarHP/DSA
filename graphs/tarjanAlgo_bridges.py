class Solution:
    # why we dont update intime because that node might be still connected to other nodes 
    # which we are yet to traverse
    
    def dfs(self, node, parent, low, tin, bridges, adj_list, visited):
        visited[node] = 1
        tin[node] = self.timer
        low[node] = self.timer
        self.timer += 1
        for adjNode in adj_list[node]:
            if adjNode == parent:
                continue # parent
            elif visited[adjNode] == 1: # could be ancestor
                low[node] = min(low[node], tin[adjNode]) # might have multiple adjnodes with ancestors
                                                         # so get minimal
            elif visited[adjNode] == 0:
                self.dfs(adjNode, node, low, tin, bridges, adj_list, visited)
                low[node] = min(low[node], low[adjNode]) # get minimal
                if low[adjNode] > tin[node]: # bridge between two nodes can have same value, so consider >, unlike articulation point
                    bridges.append([node, adjNode])

        
    def criticalConnections(self, n: int, connections):
        adj_list = [[] for i in range(n)]
        for x,y in connections:
            adj_list[x].append(y)
            adj_list[y].append(x)
        self.timer = 1
        low = [0 for i in range(n)]
        tin = [0 for i in range(n)]
        bridges = []
        visited = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, -1, low, tin,bridges, adj_list, visited)
        
        return bridges
