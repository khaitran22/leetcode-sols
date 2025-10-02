# %%
def maximumTripletValue(nums) -> int:
    max_num = max(nums[0], nums[1])
    max_diff = max(nums[0] - nums[1], 0)
    result = max_diff * nums[2]
    if len(nums) == 3:
        return result

    for i in range(3, len(nums)):
        first = max(max_diff * nums[i], result)

        # if len(nums)==3, then a1-a3 and a2-a3
        sub_max_diff = max_num - nums[i-1]
        second = sub_max_diff * nums[i]
        result = max(first, second)
        # update params
        max_diff = max(max_diff, sub_max_diff)
        max_num = max(max_num, nums[i-1])

    return result


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = max(nums[0], nums[1])
        max_diff = max(nums[0] - nums[1], 0)
        result = max_diff * nums[2]
        if len(nums) == 3:
            return result

        for i in range(3, len(nums)):
            first = max(max_diff * nums[i], result)

            # if len(nums)==3, then a1-a3 and a2-a3
            sub_max_diff = max_num - nums[i-1]
            second = sub_max_diff * nums[i]
            result = max(first, second)
            # update params
            max_diff = max(max_diff, sub_max_diff)
            max_num = max(max_num, nums[i-1])

        return result


# %%
nums = [12, 6, 1, 2, 7]
maximumTripletValue(nums)
# %%
