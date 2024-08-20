from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights) -> int:
        m = len(heights)
        n = len(heights[0])
        dist = [[1e9 for i in range(n)] for j in range(m)]

        pq = PriorityQueue()
        pq.put((0,0,0))
        dist[0][0] = 0

        dx = [0,0, 1,-1]
        dy = [1,-1,0, 0]
        while not pq.empty():
            (curr_dist , x, y) = pq.get()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                maxi = max(curr_dist, abs(heights[nx][ny] - heights[x][y]))
                if maxi < dist[nx][ny]:
                    dist[nx][ny] = maxi
                    pq.put((dist[nx][ny], nx, ny))
                else:
                    continue
        
        return dist[-1][-1]

obj = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(obj.minimumEffortPath(heights))



        