# 1. count in degree
# 2. put indegree 0 into queue; atleast one will be there for sure (acyclic)
# 3. take out element from queue
# 4. reduce indegree of its adjacent nodes
# 5. once the node gets its indegree as 0, add it into queue
# 6. after taking element out of queue, append it to ans

# visited array not needed, as it will consider indegree 0 for independent components
class Solution:   

    def kahnSort(self, n, adj_list):
        ans = []
        indegree = [0 for i in range(n)]
        for item in adj_list:
            for i in item:
                indegree[i] = indegree[i] + 1
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr_node = q.pop(0)
            ans.append(curr_node)
            for i in adj_list[curr_node]:
                indegree[i] = indegree[i] - 1
                if indegree[i] == 0:
                    q.append(i)
    
        return ans

obj = Solution()
adj_list = [[1], [0]]
n = 2
print(obj.kahnSort(n, adj_list))