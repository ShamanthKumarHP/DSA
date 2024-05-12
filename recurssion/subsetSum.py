# Pick and non pick
def subsetSum(s, i, sum_data, ans):
    if i == len(s):
        ans.append(int(sum_data))
        return 
    sum_data = sum_data + s[i]
    subsetSum(s,i+1, sum_data, ans)
    sum_data = sum_data - s[i]
    subsetSum(s,i+1, sum_data, ans)
    return ans

# s = [2,3] 
s = [3,1,2]
sum_data = 0
ans = []
print(subsetSum(s,0, sum_data, ans))