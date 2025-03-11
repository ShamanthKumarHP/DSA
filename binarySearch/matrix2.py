class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # r_low = 0
        # r_high = len(matrix) - 1

        # while (r_high >= r_low):
        #     r_mid = int((r_low + r_high)/2)

        #     if target == matrix[r_mid][0]:
        #         return True
        #     elif target < matrix[r_mid][0] :
        #         r_high = r_mid - 1
        #     else:
        #         r_low = r_mid + 1

        # c_low = 0
        # c_high = len(matrix[0])-1

        # while c_high >= c_low:
        #     c_mid = int((c_low + c_high)/2)
        #     if target == matrix[0][c_mid]:
        #         return True
        #     elif target < matrix[0][c_mid] :
        #         c_high = c_mid - 1
        #     else:
        #         c_low = c_mid + 1
        
        # print(c_high, r_high)

        # for i in range (0, r_high + 1):
        #     high = c_high
        #     low = 0
            
        #     while high >= low:
        #         mid = int((low + high)/2)
        #         print(mid)
        #         if target == matrix[i][mid]:
        #             return True
        #         elif target < matrix[i][mid] :
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        # return False


        # at [row, 0] or [0, col], 
        # i can move to one direction based value, if greater one direction
        # if lesser another direction. 
        
        col = len(matrix[0])-1
        row = 0

        while(col >= 0 and row <= len(matrix)-1):
            if(target == matrix[row][col]):
                return True
            elif(target < matrix[row][col]):
                col = col-1
            elif(target > matrix[row][col]):
                row= row + 1
        return False

obj =  Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 30
a = obj.searchMatrix(matrix, target)
print(a)




            
        
        

        
        