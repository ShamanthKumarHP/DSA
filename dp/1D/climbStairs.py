# for recursion, follow these steps to right the code
# 1. indexing
# 2. do all the stuffs
# 3. take whatever they asked min, max, or count


# for tabulation
# 1. Declare base case
# 2. express all states in for loop
# 3. copy the recurrence code and write

class Solution:
    def climbStairs(self, n: int) -> int:
        # at every step i can take either 1 step or 2 step
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # return (self.climbStairs(n-1) + self.climbStairs(n-2))


        # memoization
        # def memo(n, ds):
        #     if n <= 2:
        #         ds[n] = n
        #         return n

        #     if ds[n] != -1:
        #         return ds[n]

        #     ds[n] = memo(n-1, ds) + memo(n-2,ds)
        #     return ds[n]
        # ds = [-1] * (n+1)
        # return memo(n,ds)


        # tabulation
        # def tabu(n,ds):
        #     for i in range(3,n+1):
        #         ds[i] = ds[i-1] + ds[i-2]
        #     return ds[n]
        # ds = [-1] * (n+1)
        # ds[1] = 1
        # ds[2] = 2
        # return tabu(n,ds)
    
        # space
        def space(n):
            prev1 = 2
            prev2 = 1 
            for i in range(3, n+1):
                curr = prev1 + prev2
                prev2 = prev1
                prev1 = curr

            return prev1
        
        if n <= 2:
            return n
        
        return space(n)


object = Solution()

print(object.climbStairs(6))
print(max([1]))