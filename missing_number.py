nums = [3,0,1]

def sum_two(self, nums, target):
    hashMap = {}

    for indx, val in enumerate(nums):
        diff = target - val

        if diff in hashMap:
            return [indx, hashMap[diff]]

        hashMap[val] = indx