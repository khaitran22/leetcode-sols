def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    prev = intervals[0]
    result = []
    for i in range(1, len(intervals)):
        curr_intervals = intervals[i]
        if curr_intervals[0] >= prev[0] and curr_intervals[0] <= prev[1]:
            prev = [prev[0], max(prev[1], curr_intervals[1])]
        else:
            result.append(prev)
            prev = curr_intervals
    result.append(prev)
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [4, 5]]
# intervals = [[4, 7], [1, 4]]
# intervals = [[1, 3]]
print(merge(intervals))
