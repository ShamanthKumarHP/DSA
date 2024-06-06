
text1 = "abcd"
text2 = "abd"

def tabu():
    dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
    temp = ""
    for idx1 in range(1, len(text1)+1):
        for idx2 in range(1, len(text2)+1):
            if text1[idx1-1] == text2[idx2-1]:
                temp += text1[idx1-1]
                dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
            else:
                take1 = dp[idx1][idx2-1]
                take2 = dp[idx1-1][idx2]
                dp[idx1][idx2] = max(take1, take2) 
    return temp
print(tabu())
   