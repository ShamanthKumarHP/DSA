def rotateArray(nums, k):
    n = len(nums) - 1
    while k != 0:
        temp = nums[n]
        i = n
        while i > 0:
            nums[i] = nums [i - 1]
            i = i - 1
        nums[i] = temp
        k = k - 1
        #print(nums)
    #print(nums)
        
def rotateArrayOptimal(nums,k):
    x = 0
    y = k
    z = len(nums) - 1
    while (x<=y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
        x = x+1
        y = y-1
    print(nums)

    y = k + 1
    while (y<=z):
        temp = nums[y]
        nums[y] = nums[z]
        nums[z] = temp
        y = y + 1
        z = z-1
    print(nums)

    x = 0
    z = len(nums) -1
    while x <=z:
        temp = nums[x]
        nums[x] = nums[z]
        nums[z] = temp
        z = z -1 
        x = x + 1
    print(nums)
    
nums = [1,2,3,4,5,6,7]
k = 3
#print(nums)
#rotateArray(nums, k)
rotateArrayOptimal(nums, k)


# def reverse_nums(numr):
#     i = 0
#     j = len(numr) - 1
#     while i <=j:
#         temp = numr[i]
#         numr[i] = numr[j]
#         numr[j] = temp
#         i = i + 1
#         j = j - 1
#     return numr

# numr = [1,2,3,4,5]
# print(reverse_nums(numr))