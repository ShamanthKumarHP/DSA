#inside main i can declare array upto 10 power 6, but globally i can declare upto 10 power 7

# hashdict = {}
# s = "12332"
# for i in s:
#     if i in hashdict.keys():
#         hashdict[i] = hashdict[i] + 1
#     else:
#         hashdict[i] = 1

# print(hashdict)

from collections import defaultdict
hashdict = defaultdict(int)
s="12332"
for i in s:
    hashdict[i] = hashdict[i] + 1
print(hashdict)
