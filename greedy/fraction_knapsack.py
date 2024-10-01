def fraction_knapsack(sack, weight):
    sack = sorted(sack, key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for c_item, c_weight in sack:
        if weight - c_weight >=0 :
            weight = weight - c_weight
            ans = ans + c_item
        else:
            # take a fraction of it
            ans = ans + (c_item/c_weight)*weight
            break
    return ans


# value, weight
arr = [[200,5], [100,6], [200,2], [50,100]]
print(fraction_knapsack(arr, 80))

# arr.sort(key=lambda x : x[1], reverse=True)
# arr = sorted(arr, key = lambda x: x[0]/x[1], reverse=True)
# print(arr)
