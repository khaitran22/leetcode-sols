def threeSumClosest(nums, target) -> int:
    difference = 1e+10
    best_sum = None
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                curr_sum = nums[i]+nums[j]+nums[k]
                curr_diff = target - curr_sum
                if abs(curr_diff) < difference:
                    difference = abs(curr_diff)
                    best_sum = curr_sum
    return best_sum


nums = [-1, 2, 1, -4]
target = 1

print(threeSumClosest(nums, target))
