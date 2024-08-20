class Solution:
    def kahn(self, n, adj_list):
        # calc indegree
        indegree = [0 for i in range(n)]
        for adjs in adj_list:
            for i in adjs:
                indegree[i] = indegree[i] + 1
        
        # find indegree with 0 and add it into q
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        # decrement indegree of adjacents, make node free
        # if it becomes 0, add it into q
        ans = []
        while q:
            curr = q.pop(0)
            ans.append(curr)
            for i in adj_list[curr]:
                indegree[i] = indegree[i] - 1
                if indegree[i] == 0:
                    q.append(i)
        
        if len(ans) == n:
            return True
        return False
            
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # adj_list = { i: [] for i in range(numCourses)}
        # for pre, crs in prerequisites:
        #     adj_list[crs].append(pre)

        adj_list = [[] for i in range(numCourses)]
        for pre, crs in prerequisites:
            adj_list[crs].append(pre)
            
        
        return self.kahn(numCourses, adj_list)

obj = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(obj.canFinish(numCourses, prerequisites))

