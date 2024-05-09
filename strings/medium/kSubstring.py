# TODO
# https://www.naukri.com/code360/problems/count-with-k-different-characters_1214627?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
#  task is to return the count all the possible substrings that have exactly 'k' distinct characters.

# 'str' = abcad and 'k' = 2. 

def countSubStrings(s, k):
    cnt = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if len(set(s[i:j+1])) == k:
                cnt = cnt + 1
    return cnt


def ScountSubStrings(s,k):
    left = 0
    right = 0
    data = dict()
    ans = 0
    uniq = 0
    while right < len(s):
        if data.get(s[right], 0):
            pass
        else:
            uniq = uniq + 1
            data[s[right]] = 1

        if uniq > k:
            # to remove a unique char
            if left < len(s) -1 and s[left] != s[left+1]:
                left = left + 1
            else:
                while ( left < len(s)-1 and s[left] == s[left+1]):
                    ans = ans + 1
                    left = left + 1
                left = left + 1
                
            uniq = uniq - 1

        if uniq == k:
            ans = ans + 1
        
        right += 1
    # TODO https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/
    while left + k < len(s):
        ans = ans + 1
        left += 1
            
    return ans

st = "abcdqaaqaae"
k = 2
print(countSubStrings(st, k))
print(ScountSubStrings(st, k))