# TODO
from collections import defaultdict
class Solution:
    
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            #initialise variables
            freq_groups=defaultdict(int)
            char_freq={}
            max_freq,min_freq=1,1
            char_freq[s[i]]=1
            freq_groups[char_freq[s[i]]]=1

            for j in range(i+1,len(s)):
                if s[j] not in char_freq:
                    char_freq[s[j]]=1
                    min_freq=min(min_freq,1)
                    freq_groups[char_freq[s[j]]]+=1
                    ans+=max_freq-min_freq
                    
                else:
                    freq_groups[char_freq[s[j]]]-=1
                    if freq_groups[char_freq[s[j]]]==0 and min_freq==char_freq[s[j]]:
                        min_freq+=1
                    char_freq[s[j]]+=1
                    freq_groups[char_freq[s[j]]]+=1
                    max_freq=max(char_freq[s[j]],max_freq)
                    ans+=max_freq-min_freq
        return ans       
                

    def sbeautySum(self, s: str) -> int:
        ans = 0
        max_d = dict()
        min_d = dict()
        for i in range(len(s)):
            freq_d = dict()
            max_d = 1
            min_d = 1
            min_num = s[i]
            freq_d[s[i]] = 1

            for j in range(i+1, len(s)):
                count = freq_d.get(s[j],0)
                if count:
                    count = count + 1
                    freq_d[s[j]] = count
                    max_d = max(max_d, count)

                    if s[j] == min_num:
                        min_d +=1
                    elif count < min_d:
                        min_d = count
                        min_num = s[j]
                else:
                    freq_d[s[j]] = 1
                    min_d = 1
                    min_num = s[j]
                
                ans = ans + (max_d - min_d)
        return ans
                    






obj = Solution()
print(obj.beautySum("aaabb"))
print(obj.sbeautySum("aabb"))