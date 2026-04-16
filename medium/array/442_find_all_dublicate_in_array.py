# 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output


# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []


# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.


def findDuplicatesWithSort(nums):
    output = []
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            output.append(nums[i])
    return output


def findDuplicatesNegative(nums):
    output = []
    n = len(nums)
    for i in range(n):
        curI = abs(nums[i]) - 1
        print(curI)
        if nums[curI] < 0:
            output.append(abs(nums[i]))
        nums[curI] = -nums[curI]
        print("out", output)
    return output


values = [4, 3, 2, 7, 8, 2, 3, 1]
answer = findDuplicatesNegative(values)
print("this is the answer", answer)
