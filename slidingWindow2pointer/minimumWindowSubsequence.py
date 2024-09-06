def minimum_window_subsequence(s, t):
    # i: goes until we find all char in t
    # notedown the point
    # comes back all the way
    i = 0
    j = 0
    k = 0 # marker on s, (reversed point)
    mini = float('inf')
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        
        if j == len(t): # means found all the elements, try to traverse back now
            k = i
            j = j - 1
            while j >= 0 and k >= 0:
                if s[k] == t[j]:
                    j -= 1
                k -= 1
            k = k + 1 # take one step ahead, for actual substring
            if i - k + 1 < mini:
                mini = i - k + 1
                start_idx = k
                end_idx = i
            # reset second pointer
            j = 0

        i = i + 1
    
    return s[start_idx:end_idx+1]
    

s = "XACWEABCWCKABRC"
t = "ABC"

print(minimum_window_subsequence(s,t))