class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2

        left_half = int((n+1)/2)

        low = 0
        high = n1
        while low <= high:
            mid1 = int((low+high)/2)
            mid2 = left_half - mid1
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')

            # need to dig deep
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1,l2) + min(r1, r2))/2.0

            if l1 > r2 :
                high = mid1 - 1
            elif l2 > r1:
                low = mid1 + 1
        return 0
    
obj = Solution()
nums1 = [5,6]
nums2 = [1,2,3,4]
print(obj.findMedianSortedArrays(nums1, nums2))




        



        
        