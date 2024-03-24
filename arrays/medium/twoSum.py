nums = [2,7,11,15]
target = 9
value_idx_dict = dict()
def twoSum(nums, target):
    value_idx_dict = dict()
    for i, num in enumerate(nums):
        required_value = target - num
        key_present = value_idx_dict.get(required_value, None)
        if key_present != None:
            return [i, key_present]
        value_idx_dict[num] = i  

print(twoSum(nums, target))