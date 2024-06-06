
def recursion(str1, str2):
    def backtracking(idx1, idx2, cnt):
        if idx1 < 0 or idx2 < 0:
            return cnt
        
        if str1[idx1] == str2[idx2]:
            cnt = cnt + 1
            return backtracking(idx1-1, idx2-1, cnt)
        else:
            maxi = max(cnt, max(backtracking(idx1-1, idx2, cnt=0), backtracking(idx1, idx2-1, cnt=0)))
            return maxi
    return backtracking(len(str1)-1, len(str2)-1, cnt=0)


def memo(str1, str2):
    dp = [[-1 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    def backtracking(idx1, idx2, cnt):
        if idx1 < 0 or idx2 < 0:
            return cnt
        
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        
        if str1[idx1] == str2[idx2]:
            cnt = cnt + 1
            dp[idx1][idx2] = cnt
            return backtracking(idx1-1, idx2-1, cnt)
        else:
            maxi = max(cnt, max(backtracking(idx1-1, idx2, cnt=0), backtracking(idx1, idx2-1, cnt=0)))
            dp[idx1][idx2] = maxi
            return maxi
    return backtracking(len(str1)-1, len(str2)-1, 0)

def tabu(str1, str2):
    dp = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    maxi = 0
    for idx1 in range(1, len(str1)+1):
        for idx2 in range(1, len(str2)+1):
            if str1[idx1-1] == str2[idx2-1]:
                cnt = 1 + dp[idx1-1][idx2-1]
                dp[idx1][idx2] = cnt
            else:
                cnt = 0
                dp[idx1][idx2] = cnt
            maxi = max(maxi, cnt)
    return maxi

def spacy(str1, str2):
    prev = [0 for i in range(len(str2)+1)]
    curr = [0 for i in range(len(str2)+1)]
    maxi = 0
    for idx1 in range(1, len(str1)+1):
        for idx2 in range(1, len(str2)+1):
            if str1[idx1-1] == str2[idx2-1]:
                cnt = 1 + prev[idx2-1]
                curr[idx2] = cnt
            else:
                cnt = 0
                curr[idx2] = cnt
            maxi = max(maxi, cnt)
        prev = curr[:]
    return maxi

str1 = "abcdabcd"
str2 = "afabcdd"
print(recursion(str1, str2))
print(memo(str1, str2))
print(tabu(str1, str2))
print(spacy(str1, str2))