def findMaxConsecutiveOnes(nums):
    max_consecutives = 0
    current_max = 0
    for num in nums:
        if num == 1:
            current_max += 1
        else:
            if current_max > max_consecutives:
                max_consecutives = current_max
            current_max = 0
    return max(max_consecutives, current_max)


nums = [1, 1, 1, 1, 1, 0, 0, 0, 0]
print(findMaxConsecutiveOnes(nums))
