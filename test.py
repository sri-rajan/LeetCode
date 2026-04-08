nums = [1, 2, 3, 4, 5, 6]
n = 3
ans = []
length = len(nums)
print(n, length)
for i in range(n):
    ans.append(nums[i])
    ans.append(nums[i + n])
print(ans)
