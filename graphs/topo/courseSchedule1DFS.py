# dfs algo to check cycle

class Solution:
    def dfs(self, node, visited, path, adj_list):        
        visited[node] = 1
        path[node] = 1
    
        for i in adj_list.get(node, []):
            if visited[i] == 0:
                if self.dfs(i, visited, path, adj_list) == False:
                    return False
            elif visited[i] == 1 and path[i] == 1:
                return False
        path[node] = 0
        return True

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # idea is to detect if there's cycle(cyclic dependency)
        
        # create adjacency list
        adj_list = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        # visited array and current_path array
        visited = [0 for i in range(numCourses)]
        path = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if visited[i] == 0:
                ret = self.dfs(i, visited, path, adj_list)
                if ret == False:
                    return False
        return True


obj = Solution()
numCourses = 2
prerequisites = [[1,0], [0,1]]
print(obj.canFinish(numCourses, prerequisites))