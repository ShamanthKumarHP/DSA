class Solution:
    def get_max_element(self, mat, col):
        index = -1
        maxi = float('-inf')

        for i in range(len(mat)):
            if mat[i][col] >= maxi:
                maxi = mat[i][col]
                index = i
        return index

    def check_is_peak(self, mat, row, col):
        left = False
        right = False
        if col > 0:
            if mat[row][col] > mat[row][col-1]:
                left = True
        else:
            left = True
            
        if col < len(mat[0])-1:
            if mat[row][col] > mat[row][col+1]:
                right = True
        else:
            right = True
        return (left, right)

    def findPeakGrid(self, mat):
        low = 0
        high = len(mat[0]) - 1
        while low <= high:
            mid = int((low+high)/2)
            max_idx = self.get_max_element(mat, mid)
            check_left, check_right = self.check_is_peak(mat, row=max_idx, col=mid)
            if check_left == True and check_right ==  True:
                return [max_idx, mid]
            if check_left == False:
                high = mid - 1
            elif check_right == False:
                low = mid + 1
        return [-1, -1]

obj = Solution()
mat = [[10,20,15],[21,30,14],[7,16,32]]

print(obj.findPeakGrid(mat))






        
