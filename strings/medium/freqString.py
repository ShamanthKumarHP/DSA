# TODO learn lambda fully
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        # max_count = float('-inf')

        # count_dict = dict()
        # for i in s:
        #     count_dict[i] = count_dict.get(i, 0) + 1
        #     max_count = max(max_count, count_dict[i])
        
        # ans = ""
        # while max_count > 0:
        #     for val, freq in count_dict.items():
        #         if freq == max_count:
        #             ans = ans + val*freq
        #             count_dict[val] = 0
        
        #     max_count -= 1
        # return ans
        # n + n 

        answerString = ''
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] = hashMap[i] + 1
        # sorting the dictionary based on the values in descending order
        print(hashMap.items())
        sortedHashMap = sorted(hashMap.items(), key = lambda x: x[1], reverse=True)
        print(sortedHashMap)
        for char, frequency in sortedHashMap:
            answerString = answerString + char * frequency

        return answerString

object = Solution()
print(object.frequencySort("tree"))
        

        