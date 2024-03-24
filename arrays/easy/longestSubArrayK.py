# Find longest subarray with sum K


arr = [1,2,3,1,1,1,1]
k = 3

def lssk(arr, k):
    # dict (sum,idx)
    # calculate sum
    # take diff of sum - k
    # check if diff is present in dict 
    # take its value which represents idx
    # if not add new sum to dict

    # optimised if array has +, 0 and -
    # better if array has only + and 0
    sum_list = dict()
    sum_list[0] = -1
    total_sum = 0
    longss = 0
    for i in range(len(arr)):
        total_sum = total_sum + arr[i]
        diff = total_sum - k
        if diff in sum_list.keys():
            start_idx = sum_list[diff]
            curr_length = i - start_idx

            if curr_length > longss:
                longss = curr_length
    
        if total_sum not in sum_list.keys():
            sum_list[total_sum] = i

    return longss

print(lssk(arr,k))


def positiveLSSK(nums, k):
    # 2 pointer approach
    # move right side and calculate sum
    # if it equals to k, calculate length
    # if it exceeds k, trim from left

    i = 0
    j = 0
    n = len(nums)
    longss = 0
    total_sum = nums[0]
    while (j < n):
        # strivers
        # time complexity, below while loop will gets added
        while (total_sum > k and i <= j) :
            total_sum = total_sum - nums[i]
            i = i + 1

        if total_sum == k :
            longss =  max(longss, j - i + 1)

        j = j + 1
        if j < n:
            total_sum = total_sum + nums [j]

        #shamanth
        # if total_sum == k:
        #     longss = max(longss, j - i + 1)

        # if total_sum > k and i < j:
        #     total_sum = total_sum - nums[i]
        #     i = i + 1
        #     continue
        # j = j + 1
        # if j < n:
        #     total_sum = total_sum + nums [j]
    return longss

# TC 
# one o(n) for right pointer, one o(n) for left pointer worst case.
# o(2n) => o(n)

print(positiveLSSK(arr , k))