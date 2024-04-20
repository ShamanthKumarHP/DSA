class Solution:
    def merge(self, arr, low, mid, high):
        temp = []  # temporary array
        i = low  # starting index of left half of arr
        j = mid + 1  # starting index of right half of arr

        # storing elements in the temporary array in a sorted manner
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        # if elements on the left half are still left
        while i <= mid:
            temp.append(arr[i])
            i += 1

        # if elements on the right half are still left
        while j <= high:
            temp.append(arr[j])
            j += 1

        # transferring all elements from temporary to arr
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
    def countPairs(self, arr, low, mid, high):
        right = mid + 1
        cnt = 0
        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += (right - (mid + 1))
        return cnt

    def mergeSort(self, arr,low,high):
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(arr, low, mid)  # left half
        cnt += self.mergeSort(arr, mid + 1, high)  # right half
        cnt += self.countPairs(arr, low, mid, high)  # Modification
        self.merge(arr, low, mid, high)  # merging sorted halves
        return cnt

    def reversePairs(self, nums):
        # cnt = 0
        # i = 0
        # n = len(nums)
        # while i < len(nums) - 1:
        #     j = i + 1
        #     first = nums[i]
        #     while j < len(nums):
        #         second = nums[j]
        #         if first > 2 * second:
        #             cnt = cnt + 1
        #         j = j + 1
        #     i = i + 1
        # return cnt

        low = 0
        high = len(nums) - 1
        cnt = self.mergeSort(nums, low, high)
        return cnt
    
obj = Solution()
nums = [1,3,2,3,1]
print("ans", obj.reversePairs(nums))