#  TC = 4*alpha => constant
class Disjoint:
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


    
V=7
# obj = Solution(7)
# obj.unionByRank([1,2])
# obj.unionByRank([2,3])
# obj.unionByRank([4,5])
# obj.unionByRank([6,7])
# obj.unionByRank([5,6])
# # if obj.getUltimateParent(3) == obj.getUltimateParent(7):
# #     print("same component")
# # else:
# #     print("not same")

# obj.unionByRank([3,7])

# if obj.getUltimateParent(3) == obj.getUltimateParent(7):
#     print("same component")
# else:
#     print("not same")

# print("rank", obj.rank)
# print("parent", obj.parent)

print("\nunion by size")

V=7
obj = Disjoint(7)
obj.unionBySize([1,2])
obj.unionBySize([2,3])
obj.unionBySize([4,5])
obj.unionBySize([6,7])
obj.unionBySize([5,6])
# if obj.getUltimateParent(3) == obj.getUltimateParent(7):
#     print("same component")
# else:
#     print("not same")

obj.unionBySize([3,7])

print(obj.getUltimateParent(2))
print(obj.getUltimateParent(6))
if obj.getUltimateParent(1) == obj.getUltimateParent(6):
    print("same component")
else:
    print("not same")


print("size", obj.size)
print("parent", obj.parent)
        

            

