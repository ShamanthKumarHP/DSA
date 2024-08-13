# bfs and dfs code is here

def bfs(node, adj, visited):
    stack = []
    stack.append((node, -1))
    visited[node] = 1
    ans = False
    while stack:
        (curr, parent) = stack.pop(0)
        for next in adj[curr]:
            if visited[next] == 0:
                visited[next] = 1
                stack.append((next, curr))
            elif next != parent:
                ans = True
                break
    return ans

def solutionBFS(v, adj):
    # what if it contains components
    visited = [0] * v
    for node in range(v):
        if visited[node] == 0:
            if bfs(node, adj, visited) == True:
                return True
    return False

def dfs(node, adj, visited, parent):
    visited[node] = 1
    for next in adj[node]:
        if visited[next] == 0:
            if dfs(next, adj, visited, node) == True:
                return True
        elif next != parent:
            return True
    return False

def solutionDFS(v,adj):
    visited = [0] * v
    for node in range(v):
        if visited[node] == 0:
            if dfs(node, adj, visited, -1) == True:
                return True
    return False

V = 3
E = 2
adj = [[1], [0, 2],[1]]

print(solutionBFS(V, adj))
print(solutionDFS(V, adj))