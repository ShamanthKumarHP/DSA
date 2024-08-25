# prims + disjoinSet
# sort the edges 
# check if its of same component


class Solution:
    def __init__(self, V) -> None:
        self.rank = [0 for i in range(V+1)] # just to support 1 base indexing
        self.parent = [i for i in range(V+1)]

        self.size = [1 for i in range(V+1)]

    # path compression
    def getUltimateParent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.getUltimateParent(self.parent[u])
        return self.parent[u]
    

    def unionByRank(self, edge):
        x, y = edge[0], edge[1]

        x_up = self.getUltimateParent(x)
        y_up = self.getUltimateParent(y)

        # both belong to same component already
        if x_up == y_up:
            return
        
        if self.rank[x_up] < self.rank[y_up]:
            self.parent[x_up] = y_up
        elif self.rank[x_up] > self.rank[y_up]:
            self.parent[y_up] = x_up
        else: # same rank
            self.parent[y_up] = x_up
            self.rank[x_up] = self.rank[x_up] + 1

    def unionBySize(self, edge):
        x, y = edge[0], edge[1]

        x_up = self.getUltimateParent(x)
        y_up = self.getUltimateParent(y)

        if self.size[x_up] > self.size[y_up]:
            self.parent[y_up] = x_up
            self.size[x_up] = self.size[x_up] + self.size[y_up]
        elif self.size[x_up] < self.size[y_up]:
            self.parent[x_up] = y_up
            self.size[y_up] = self.size[y_up] + self.size[x_up]
        else:
            self.parent[y_up] = x_up
            self.size[x_up] = self.size[x_up] + self.size[y_up]


def kruskalAlgo(V, edges):
    new_edges = []
    for u in range(V):
        for v,w in edges[u]:
            new_edges.append(w, u, v)
    new_edges.sort()

    mst = 0
    Disjoint = Solution(V)
    for w,u,v in new_edges:
        u_ulp = Disjoint.getUltimateParent(u)  # 4 alpha
        v_ulp  = Disjoint.getUltimateParent(v)
        if u_ulp == v_ulp:
            # nothing to as they belong to same component
            continue
        mst += w
        Disjoint.unionByRank([u,v]) # 4 alpha

    return mst

#  TC = O( V+E   +   ElogE   +     E*4 alpha * 2)
#  SC = V + V + E



