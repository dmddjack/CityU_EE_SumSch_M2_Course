def product_array(array):
    new_array = array[:]
    for i in range(len(array)):
        for j in range(len(new_array)):
            new_array[j] *= array[i]
        new_array[i] /= array[i] ** 2
    return new_array


print(product_array([1, 2, 3, 4, 5]))  # result: [120, 60, 40, 30, 20]
print(product_array([1, 2, 3]))  # result: [6, 3, 2]
print(product_array([1, 1, 2, 3, 5, 8, 13]))   # result: [3120, 3120, 1560, 1040, 624, 390, 240]
