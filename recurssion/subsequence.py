# NOTE pick followup elements
def subsequence(s, temp, i):
    if i >= len(s):
        print(temp)
        return s
    char = s[i]
    temp.append(char)
    subsequence(s, temp, i+1)
    temp.remove(char)
    subsequence(s, temp, i+1)
    return


s = [1,2,3,4,5]
temp = []
# subsequence(s,temp, 0)
# TC 2*N



def subsequence_with_sum_k(s, temp, i, tempSum, k):
    if tempSum == k and i < len(s):
        print(temp)
        return

    if i >= len(s):
        return
    
    char = s[i]
    tempSum = tempSum + char
    temp.append(char)
    subsequence_with_sum_k(s, temp, i+1, tempSum, k)
    temp.remove(char)
    tempSum = tempSum - char
    subsequence_with_sum_k(s, temp, i+1, tempSum, k)
    return


s = [1,2,3,4,5]
temp = []
tempSum = 0
k = 3
subsequence_with_sum_k(s,temp, 0, tempSum, k)
# TC 2*N