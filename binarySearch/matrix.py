# to find target in m * n sorted matrix 

matrix = [[1,2,3],[4,5,6],[7,8,9]]


def searchMatrix(matrix, target) -> bool:
    r_low = 0
    c_low = 0
    r_high = len(matrix) - 1
    c_high = len(matrix[0]) - 1
    target_row = -1
    target_column = -1

    while (r_high>=r_low):
        r_mid = int((r_low + r_high)/2)
        if target <= matrix[r_mid][c_high] and target >= matrix[r_mid][0]:
            target_row = r_mid
            break
        elif target < matrix[r_mid][0]:
            r_high = r_mid - 1
        else:
            r_low = r_mid + 1

    while (c_high >= c_low):
        c_mid = int((c_low+c_high)/2)
        if target == matrix[target_row][c_mid]:
            target_column = c_mid
            break
        if target < matrix[target_row][c_mid]:
            c_high = c_mid - 1
        else:
            c_low = c_mid + 1

    if target_column != -1:
        return True
    else:
        return False


m = len(matrix)
n = len(matrix[0]) 
print(f'matrix has {m} rows and {n} columns')

target = 1
print(searchMatrix(matrix, target))

