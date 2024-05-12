def allPermutation(nums, ds, freq, ans):
    if len(ds) == len(nums):
        ans.append(ds[:])
        return 
    for i in range(len(nums)):
        if not freq.get(i,False):
            freq[i] = True
            ds.append(nums[i])
            allPermutation(nums, ds, freq, ans)
            ds.pop()
            freq[i] = False
    return ans



nums = [1,2,3]
print(allPermutation(nums, [], {}, []))

# number of permutation is n! 

# TC: n! * n (appending)
# SC: n! (ans) + n (ds) + n (freq map)
# Auxillay SC: n

# optimal
# reduce space
def permutation_by_swapping(start, nums, ans):
    if start == len(nums):
        ans.append(nums[:])
        return
    
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        # increment pointed to next place
        permutation_by_swapping(start+1, nums, ans)
        # reswap -> back to original
        nums[start], nums[i] = nums[i], nums[start]
    return ans

nums = [1,2,3]

print(permutation_by_swapping(0, nums, []))