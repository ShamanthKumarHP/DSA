# find number of subarrays who has XOR as K

arr = [4,2,2,6,4]
k = 6

'''
calculate xor when traversing(XR), 
if we want to find whether we had k at a point, 
then we have to see if there is anyones(elements x) that i can xor with my XOR to get K


[4,2,2,6,4]
<--------XR>
<--x><----k>
<---|<----k>
Remember xor of same numbers is zero
'''

front_xor = dict()
# to store total xor and store count
front_xor[0] = 1
xor = 0
arr = [4,2,2,6,4]
k = 6
cnt = 0
total_xor = 0
# for i in arr:
#     total_xor = total_xor ^ i
#     needed_xor = total_xor ^ k
#     get_cnt = front_xor.get(needed_xor,0)
#     if get_cnt:
#         cnt = cnt + get_cnt
#     if front_xor.get(total_xor, 0):
#         front_xor[total_xor] = front_xor[total_xor] + 1
#     else:
#         front_xor[total_xor] = 1

# made it simple

for i in arr:
    total_xor = total_xor ^ i
    needed_xor = total_xor ^ k
    cnt = cnt + front_xor.get(needed_xor,0)
    front_xor[total_xor] = front_xor.get(total_xor, 0) + 1
print(cnt)
 





    


