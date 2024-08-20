# concept is simple, use example with time period for better understanding of algorithm
# travel to nodes with less time and relax its neighbours
from queue import PriorityQueue
class Solution:
    def usingPR(self, V, src, adj_list):
        pq = PriorityQueue()
        distance_list = [1e9 for i in range(V)]

        pq.put((0, src))
        distance_list[src] = 0

        while not pq.empty(): # V
            nodeWeight, node = pq.get() #log(HeapSize)
            # relax neighbours
            for peer, weight in adj_list[node]: # ne
                relax_dist = distance_list[node] + weight
                if distance_list[peer] > relax_dist:
                    distance_list[peer] = relax_dist
                    pq.put((relax_dist, peer)) #log(HeapSize)

        return distance_list
    # cons: if we get duplicate nodes with higher time period, we will still traverse through those values
    # to make sure we dont get any duplicates, we will use set
    #  TC derivation
    # WKT total edges (E) = V * V(-1) => V2
    # heapsize = may go upto V*V
    # V ( log(HeapSize) + total_num of edges * log(HeapSize))
    # V ( log(HeapSize) [1 + ne])
    # V ( log(HeapSize) (1+ V-1))
    # V ( log(HeapSize) * V)
    # V2 * log(HeapSize)
    # V2 * log(V2)
    # V2 * 2 log(V)
    ## E * 2 log(V)
    ## E*log(V)


    # TC: 
    def usingSet(self, V, src, adj_list):
        pqs = set()
        distance_list = [1e9 for i in range(V)]

        pqs.add((0, src)) # logN
        distance_list[src] = 0

        while pqs:
            nodeWeight, node = pqs.pop() #logN
            for peer, weight in adj_list[node]:
                relax_dist = distance_list[node] + weight
                if relax_dist < distance_list[peer]:
                    if distance_list[peer] == 1e9:
                        # first to reach
                        distance_list[peer] = relax_dist
                        pqs.add((relax_dist, peer))
                    else:
                        # means already someone visited and yet to be done relaxation
                        # higher value item is present in set, 
                        # remove it and add curr since it is optimised
                        pqs.discard((distance_list[peer], peer)) # no exception
                        distance_list[peer] = relax_dist
                        pqs.add((relax_dist, peer))

        return distance_list
    
    def usingQ(self, V, src, adj_list):
        q = []
        distance_list = [1e9 for i in range(V)]
        
        q.append((0, src))
        distance_list[src] = 0
        while q:
            nodeWeight, node = q.pop(0)
            for peer, weight in adj_list[node]:
                relax_dist = distance_list[node] + weight
                if relax_dist < distance_list[peer]:
                    distance_list[peer] = relax_dist
                    q.append((relax_dist, peer))
                
        return distance_list
    
obj = Solution()

src = 2
V = 3
adj_list = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
print(obj.usingPR(V, src, adj_list))
print(obj.usingSet(V, src, adj_list))
print(obj.usingQ(V, src, adj_list))
