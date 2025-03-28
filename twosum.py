def twoSum(nums, target):
    list_length = len(nums)
    for i in range(list_length): #0, 1, 2, 3, 4
        for j in range(i, list_length): #0, 1, 2, 3, 4, 5, 6
            if(nums[i] + nums[j] == target):
                return [i, j]

print(twoSum([3, 4, 2],  6))








