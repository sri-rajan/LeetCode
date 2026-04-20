# 239. Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


# brute force
def maxSlidingWindow(nums, k):
    n = len(nums)
    l = 0
    r = k
    maxList = [0] * (n - k + 1)
    maxList[0] = nums[0]
    curIndex = 0
    while r <= n:
        print("this is l and r", l, r)
        curMax = nums[l]
        for i in range(l, r):
            curMax = max(curMax, nums[i])
        maxList[curIndex] = curMax
        curIndex += 1
        r += 1
        l += 1

    return maxList


# optimized way
from collections import deque


def maxSlidingWindow2(nums, k):
    dq = deque()
    res = []
    n = len(nums)
    for i in range(n):
        print("this is dq", dq, i)
        if dq and dq[0] <= i - k:
            dq.popleft()
        print("this is dq2", dq)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        print("this is dq3", dq)
        dq.append(i)
        print("this is dq4", dq)
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res


values = [1, 3, 1, 2, 0, 5]  # [3,3,2,5]
k = 3
answer = maxSlidingWindow2(values, k)
print("this is answer", answer)
