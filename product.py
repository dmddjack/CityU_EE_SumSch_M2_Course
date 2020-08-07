def product_array(array):
    new_array = array[:]
    for i in range(len(array)):
        for j in range(len(new_array)):
            new_array[j] *= array[i]
        new_array[i] /= array[i] ** 2
    return new_array


print(product_array([1, 2, 3, 4, 5]))
