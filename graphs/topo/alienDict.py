class Solution:
    def alien(self, words,N,K):
        # first create a adj_list by comparing adjacent words
        adj_list = [[] for i in range(K)]
        i = 0
        while i < K-1:
            s1 = words[i]
            s2 = words[i+1]
            l = min(len(s1), len(s2))
            for i in range(l):
                if s1[i] != s2[i]:
                    adj_list[ord(s1[i]) - 97].append(ord(s2[i]) - 97)
                    break

                if i == l-1:
                    if len(s1) > len(s2):
                        return "invalid"
            
            i = i + 1
        
        indegree = [0 for i in range(K)]
        for connect in range(K):
            for item in adj_list[connect]:
                indegree[item] = indegree[item] + 1
        
        q=[]
        for i in range(K):
            if indegree[i] == 0:
                q.append(i)

        ans = []
        while q:
            curr = q.pop(0)
            ans.append(curr)
            for item in adj_list[curr]:
                indegree[item] = indegree[item] - 1
                if indegree[item] == 0:
                    q.append(item)
    
        final = []
        for i in ans:
            final.append(chr(97 + i))

        if len(final) != K:
            return "invalid"
    
        return final
    

N = 5 # total words in list
K = 4 # total english words
words = ["baa","abcd","abca","cab","cad"]
# Given a sorted dictionary of an alien language having N words and k starting alphabets of a standard dictionary.
# Find the order of characters in the alien language.

obj = Solution()
print(obj.alien(words, N, K))

# follow up
# what if the given dictionary is invalid




