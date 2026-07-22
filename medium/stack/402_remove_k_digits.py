# 402. Remove K Digits
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


# Constraints:

# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.


def removeKdigits(num, k):
    if len(num) <= k:
        return "0"
    stack = []
    curK = k
    for i in num:
        while curK and len(stack) and stack[-1] > i:
            stack.pop()
            curK -= 1
        stack.append(i)
    while curK:
        if not len(stack):
            break
        stack.pop()
        curK -= 1
    return "".join(stack).lstrip("0") or "0"


num = "33526221184202197273"
k = 19
ans = removeKdigits(num, k)
print("this is the ans", ans)
