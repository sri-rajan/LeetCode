# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.


# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


def merge(intervals):
    # sort by first values
    # compare last and first of susequent
    sorted_value = sorted(intervals, key=lambda x: x[0])
    final_output = []
    n = len(sorted_value)
    curr = 1
    overlap = sorted_value[0]
    print("thisi s sortedval", sorted_value)
    while curr <= n:
        if curr == n:
            final_output.append(overlap)
            break
        print(overlap)
        if sorted_value[curr][0] <= overlap[1]:
            overlap[1] = max(sorted_value[curr][1], overlap[1])
        else:
            final_output.append(overlap)
            overlap = sorted_value[curr]
        curr += 1
    return final_output


values = [[1, 4], [2, 3]]
answer = merge(values)
print("This is merge Answer", answer)
