# https://takeuforward.org/arrays/minimise-maximum-distance-between-gas-stations/
# https://www.naukri.com/code360/problems/minimise-max-distance_7541449?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

"""
Problem statement
You are given a sorted array 'arr' of length 'n', which contains positive integer positions of 'n' gas stations on the X-axis.
You are also given an integer 'k'.
You have to place 'k' new gas stations on the X-axis.
You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions.
Let 'dist' be the maximum value of the distance between adjacent gas stations after adding 'k' new gas stations.
Find the minimum value of dist.

Example:
Input: 'n' = 7 , 'k'=6, 'arr' = {1,2,3,4,5,6,7}.
Answer: 0.5
Explanation:
We can place 6 gas stations at 1.5, 2.5, 3.5, 4.5, 5.5, 6.5. 

Thus the value of 'dist' will be 0.5. It can be shown that we can't get a lower value of 'dist' by placing 6 gas stations.

Note:
You will only see 1 or 0 in the output where:
  1 represents your answer is correct.
  0 represents your answer is wrong. 
Answers within 10^-6 of the actual answer will be accepted.
"""

# brute force

def findGasStation(arr, k):
    n = len(arr)
    # to store how many gas stations is present in a section
    howMany = [0] * (n-1)

    for gasStation in range(1, k+1):
        maxDist = -1
        section = -1
        for i in range(0,n-1):
            dist = (arr[i+1] - arr[i]) / (howMany[i]+1)
            if dist >= maxDist:
                maxDist = dist
                section = i
        
        howMany[section] += 1

    # calculate maximum distance
    maxDist = -1
    for i in range(0,n-1):
        dist = (arr[i+1] - arr[i]) / (howMany[i]+1)
        if dist >= maxDist:
            maxDist = dist

    return maxDist

arr = [1,2,3,4,5,6,7]
k = 6
# print(findGasStation(arr, k))

# TC = N * K * N


# better solution 
# trying to find some logic to get maximum section gap quickly with its index
# use priority queue

# note we are multiplying by -1 when we store in heap, because by default heap will only store smallest value at the top 
# whatever items follows , it is not in order

import heapq
def better_findGasStation(arr, k):
    n = len(arr)
    howMany = [0] * (n-1)
    pq = []
    for i in range(0, n-1):
        diff = arr[i+1] - arr[i]
        heapq.heappush(pq, (-1*diff,i))
    print(pq)
    for gasStation in range(k):
        dist, section = heapq.heappop(pq)
        howMany[section] += 1

        re_calculate_dist = (arr[section+1]-arr[section]) / (howMany[section] + 1)

        heapq.heappush(pq, (-1*re_calculate_dist, section))
    return pq[0][0]*(-1)

arr = [1,2,3,4,5,6]
k = 5
print(better_findGasStation(arr, k))

# TC =O( Nlog(N) + K logN )


# optimal solution using BS

def checkNumberOfGasStation(arr, mid):
    cnt = 0
    
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        possible_gs = diff/mid

        # if it gets divided without giving any remainder
        # for eg: in 1,2,3 arr
        # dist 1
        # if i take mid as 0.5
        # then 1/0.5 gives 2, which means 2 gas stations are possible with 0.5 dist which is wrong so. 
        # in good case, there will be always some remainder so 1/0.4 gives value 2 which means we can 2 gs. 1.4 and 1.8
        if (diff == possible_gs * mid):
            possible_gs = possible_gs - 1
        
        cnt = cnt + possible_gs

    return cnt

def bs_gasStation(arr, k):
    n = len(arr)
    ans = -1
    low = 0
    high = -1
    for i in range(n-1):
        if (arr[i+1] - arr[i]) > high:
            high = arr[i+1] - arr[i]
    while high - low > 1e-6:
        mid = (low+high)/2
        num_of_gs = checkNumberOfGasStation(arr, mid)
        if num_of_gs > k:
            low = mid
        else:
            ans = mid
            high = mid
    return ans

arr = [1,2,3,4,5,6]
k = 5
print("bs_gasStation", bs_gasStation(arr, k))




