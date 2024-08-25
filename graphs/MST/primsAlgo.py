
# Steps
# 1. Mark the visited array as 0 for all the nodes

# 2. Start with 0th node and push
# (0,0,-1)
# explanation:  -1 means 0 is the genesis node
# Mark 0 as visited

# 3. Push all the neighbours of 0 in pq Do not mark them visited  (footnote 1)
# Since its a min heap the edge with minimum weight will be at the top

# 4. Pick up the top edge , insert it in the mst , mark the picked node as visited , insert all neighbours of picked node into pq

# 5. keep repeating steps 3 and 4 untill all the nodes have been picked up and thats when the algorithm ends

from queue import PriorityQueue
def primALgo(V, adj_list):
    visited = [0 for i in range(V)]
    sum = 0
    pq = PriorityQueue()
    mst = []
    pq.put((0,0,-1)) # weight, node, parentNode

    while not pq.empty():
        weight, currNode, parentNode = pq.get()
        if visited[currNode] == 1:
            continue

        if parentNode != -1:
            mst.append([currNode, parentNode])
        
        visited[currNode] = 1
        sum = sum + weight
        for u,w in adj_list[currNode]:
            if visited[u] == 0:
                pq.put((w, u, currNode))

    return sum