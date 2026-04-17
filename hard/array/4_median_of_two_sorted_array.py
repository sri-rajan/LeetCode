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


def findMedianSortedArraysOptimized(nums1, nums2):
    A, B = nums1, nums2
    aLen = len(nums1)
    bLen = len(nums2)
    if aLen > bLen:
        A, B = B, A
        aLen, bLen = bLen, aLen
    total = aLen + bLen
    half = total // 2
    l, r = 0, aLen - 1
    while True:
        Amid = (l + r) // 2
        Bmid = half - Amid - 2  # minus 2 because of index

        Aleft = A[Amid] if Amid >= 0 else float("-infinity")
        Aright = A[Amid + 1] if Amid + 1 < aLen else float("infinity")
        Bleft = B[Bmid] if Bmid >= 0 else float("-infinity")
        Bright = B[Bmid + 1] if Bmid + 1 < bLen else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2 == 0:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            return min(Aright, Bright)
        elif Aleft < Bright:
            l += 1
        else:
            r -= 1


nums1 = []
nums2 = [2, 3]
answer = findMedianSortedArraysOptimized(nums1, nums2)
print("this is the answer", answer)
