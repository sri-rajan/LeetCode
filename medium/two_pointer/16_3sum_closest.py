# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.


# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


def threeSumClosest(nums, target):
    closetVal = None
    n = len(nums)
    nums.sort()
    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > target:
                k -= 1
            elif sum < target:
                j += 1
            if not closetVal:
                closetVal = sum
            if abs(closetVal - target) > abs(sum - target):
                closetVal = sum
            if closetVal == target:
                return closetVal

    return closetVal


values = [-4, 2, 2, 3, 3, 3]
ans = threeSumClosest(values, 0)
print("this is answer", ans)
