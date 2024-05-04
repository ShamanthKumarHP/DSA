class Solution:
    def longestCommonPrefix(self, strs):
        longest_common = ""
        j = 0
        while True:
            if j < len(strs[0])+1:
                temp_common = strs[0][:j]
            else:
                break
            for i in strs[1:]:
                if not j < len(i)+1 or temp_common != i[:j]:
                    return longest_common
            longest_common = temp_common
            j = j + 1
        return longest_common
    
    def SortinglongestCommonPrefix(self, strs):
        arr = sorted(strs)
        first = arr[0]
        last = arr[-1]
        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans = ans + first[i]
        return ans
object = Solution()
print(object.longestCommonPrefix(["flower","flow","flight"]))
print(object.SortinglongestCommonPrefix(["flower","flow","flight"]))
print("a"*3)