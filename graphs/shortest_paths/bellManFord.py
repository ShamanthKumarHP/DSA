# If the graph has negative cycle
# If the graph contains negative edges.

# TC V*E

def bellMan(V, src, edges):
    dist = [1e9 for i in range(V)]
    dist[src] = 0
    # only V-1 times relaxation it should perform
    for i in range(V-1):
        for u, v, weight in edges:
            if dist[u] != 1e9 and dist[u] + weight < dist[v] :
                dist[v] = dist[u] + weight

    # if any negative cycle
    for u,v, weight in edges:
        if dist[u] != 1e9 and dist[u] + weight < dist[v]:
            return -1
    
    return dist

    