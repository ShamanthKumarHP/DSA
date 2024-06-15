# increase + decreasing subseq
# or increasing
# or decreasing


nums = [1,2,3,10,3,1]
n = len(nums)
dp1 = [1] * n
dp2 = [1] * n


for i in range(n):
    for prev_idx in range(i):
        if nums[i] > nums[prev_idx] and dp1[prev_idx]+1 > dp1[i]:
                dp1[i] = dp1[prev_idx]+1
                

for i in range(n-1, -1, -1):
    for prev_idx in range(n-1, i-1, -1):
        if nums[i] > nums[prev_idx] and dp2[prev_idx]+1 > dp2[i]:
                dp2[i] = dp2[prev_idx]+1

maxi = 0
for i in range(n):
     bitonic = dp1[i] + dp2[i] -1 # common
     if bitonic > maxi:
          maxi = bitonic
print(maxi)