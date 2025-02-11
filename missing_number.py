nums = [3,0,1]

def sum_two(nums, target):
    hashMap = {}

    for indx, val in enumerate(nums):
        diff = target - val

        if diff in hashMap:
            return [indx, hashMap[diff]]

        hashMap[val] = indx

result = sum_two(nums, 4)
print(result)