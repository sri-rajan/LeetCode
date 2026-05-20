# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


# optimized way
def trap(height):
    n = len(height)
    l = 0
    r = n - 1
    lmax = 0
    rmax = 0
    total_water = 0
    while l < r:
        if lmax <= rmax:
            l += 1
            lmax = max(lmax, height[l])
            total_water += lmax - height[l]
        else:
            r -= 1
            rmax = max(rmax, height[r])
            total_water += rmax - height[r]
    return total_water


def trap2(height):
    n = len(height)
    lmaxList = [0] * n
    rmaxList = [0] * n
    lmaxList[0] = height[0]
    rmaxList[n - 1] = height[n - 1]
    waterlevel = 0
    for i in range(1, n - 1):
        lmaxList[i] = max(height[i], lmaxList[i - 1])
    for i in range(n - 2, 0, -1):
        rmaxList[i] = max(height[i], rmaxList[i + 1])
    for i in range(1, n - 1):
        minval = min(lmaxList[i], rmaxList[i])
        if height[i] < minval:
            waterlevel += min(lmaxList[i], rmaxList[i]) - height[i]
    return waterlevel


values = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
answer = trap2(values)
print("this is answer", answer)
