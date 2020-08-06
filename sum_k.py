def sumk(nums, k):
    list1 = []
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                list1.append((nums[i], nums[j]))
                count += 1
    if count == 0:
        print('no results')
    else:
        for i in range(count):
            print('{0} + {1} = {2}'.format(list1[i][0], list1[i][1], k))


sumk([1, 2, 3, 4], 5)
print()
sumk([1, 2, 3, 4], 8)
