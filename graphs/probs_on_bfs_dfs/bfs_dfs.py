#TC : V+E
class ClassNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def add_nodes():
        return

    def BFS_traversal(self, node, adj_list):
        stack = []
        stack.append(node)
        visit = dict()
        visit[node] = 1
        ans = []
        while stack:
            node = stack.pop(0)
            ans.append(node)
            adj_nodes = adj_list[node]
            for ele in adj_nodes:
                if not visit.get(ele, None):
                    visit[ele] = 1
                    stack.append(ele)
        return ans
    
    def DFS_traversal(self, node, adj_list):
        ans = []
        visited = dict()
        def dfs(node):
            visited[node] = 1
            ans.append(node)
            adj_nodes = adj_list[node]
            for ele in adj_nodes:
                if not visited.get(ele, None):  
                    dfs(ele)
            return
        dfs(node)
        return ans

                


        
