import heapq


def findKthLargest(nums, k):
    class Pair:
        def __init__(self, k, v):
            self.k = k
            self.v = v

        def __lt__(self, other):
            return self.k < other.k
    # With sorting
    # nums = sorted(nums)
    # return nums[len(nums)-k]

    # Without sorting
    counter = {}
    for num in nums:
        if counter.get(num) == None:
            counter[num] = 1
        else:
            counter[num] = counter[num] + 1

    arr = [Pair(k, v) for k, v in counter.items()]
    heapq.heapify(arr)
    target = len(nums) - k
    curr_pos = 0
    for i in range(len(arr)):
        pair = heapq.heappop(arr)
        curr_pos += pair.v
        if curr_pos-1 >= target:
            return pair.k


nums = [3, 2, 1, 5, 6, 4]
k = 2
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
print(findKthLargest(nums, k))
