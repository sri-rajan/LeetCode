# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


def findMedianSortedArrays(nums1, nums2):
    lastTwo = [0, 0]
    m = len(nums1)
    n = len(nums2)
    if m == 0 and n == 1:
        return nums2[0]
    if n == 0 and m == 1:
        return nums1[0]
    totalSize = m + n
    mid = totalSize / 2
    neededdata = int(mid) if mid == int(mid) else int(mid) + 1
    current = 0
    left, right = 0, 0
    while current <= neededdata:
        crtValue = None
        if left < m and right < n:
            if nums1[left] < nums2[right]:
                crtValue = nums1[left]
                left += 1
            else:
                crtValue = nums2[right]
                right += 1
        elif left >= m:
            crtValue = nums2[right]
            right += 1
        else:
            crtValue = nums1[left]
            left += 1

        if current % 2 == 0:
            lastTwo[0] = crtValue
        else:
            lastTwo[1] = crtValue
        current += 1
        print(lastTwo, crtValue, "this is tttt")

    return min(lastTwo) if totalSize % 2 != 0 else sum(lastTwo) / 2


nums1 = []
nums2 = [2, 3]
answer = findMedianSortedArrays(nums1, nums2)
print("this is the answer", answer)
