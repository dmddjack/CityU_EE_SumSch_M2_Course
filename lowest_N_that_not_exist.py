def lowest_n_that_not_exist(array):
    for pos_integer in range(len(array)):
        if pos_integer + 1 not in array:
            return pos_integer + 1


print(lowest_n_that_not_exist([1, 2, 3, 3, 4, -5, 7, 7]))
print(lowest_n_that_not_exist([3, 4, -1, 1]))
print(lowest_n_that_not_exist([1, 2, 0]))

