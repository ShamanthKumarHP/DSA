# priority queue with chepest price as key will not work
# if we have found a better price of a city, but moving forward if we cannot reach dst in that path
# then we cannot have the same price for that city.
# hence we have to use stops as key here
# if we enough stops, then we can find best price for the city
# since we are lineraly going with stops(BFS), queue is fine
# stops is the constraint here.

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # create adj list
        adj_list = [[] for i in range(n)]
        for sp, ep, price in flights:
            adj_list[sp].append([ep, price])
        
        pq = []
        pq.append((k, 0, src)) # remainingStops, price, city
        cheapestPrices = [1e9 for i in range(n)]
        cheapestPrices[src] = 0

        while pq:
            stops, price, city = pq.pop(0)
            if stops < 0:
                continue
            for connects in adj_list[city]:
                conn, pay = connects[0], connects[1]
                if price + pay < cheapestPrices[conn]:
                    cheapestPrices[conn] = price + pay
                    pq.append((stops-1, price+pay, conn))
        if cheapestPrices[dst] != 1e9:
            return cheapestPrices[dst]
        return -1  
        