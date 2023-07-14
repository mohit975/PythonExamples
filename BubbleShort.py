def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range (len(array) -i -1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
    return array


    print(array)

array = [10, 5, 2, 7, 3, 1, 8, 9, 6,10, 5, 2, 7, 3, 1, 8, 9, 6]

print(bubble_sort(array))