class Celebrity:
    def naive(self, n, matrix):
        knowMe = [0 for i in range(n)]
        iknow = [0 for i in range(n)] # i know someone
        for r in range(n):
            for c in range(n):
                if matrix[r][c] == 1:
                    knowMe[c] += 1
                    iknow[r] = 1
        
        for i in range(n):
            if knowMe[i] == n-1 and iknow[i] == 0:
                return i
        return 0

    def best(self, n, matrix):
        top = 0
        bottom = n-1
        while top < bottom: #o(N)
            if matrix[top][bottom] == 1:
                top += 1
            elif matrix[bottom][top] == 1:
                bottom -= 1
            # elif matrix[top][bottom] == 0 and matrix[bottom][top]: same
            else:
                top += 1
                bottom -= 1
        
        if top < bottom:
            return -1
        
        for i in range(n): #o(N)
            # scan whole row and column
            if i == top:
                continue
            elif matrix[top][i] == 0 and matrix[i][top] == 1:
                continue
            else:
                return -1
        return top
            
obj = Celebrity()
matrix = [[]]
n = len(matrix[0])
print(obj.naive(n, matrix))