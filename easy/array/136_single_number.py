def compute(nums):
    data = {}
    for i in nums:
        print("this i si", i)
        if i in data:
            del data[i]
        else:
            data[i] = True
    print("thius is", list(data.keys())[0])


vals = [1, 1, 2, 3, 3, 4, 4]
compute(vals)
