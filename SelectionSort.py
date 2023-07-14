"""
Selection sort is a simple sorting algorithm that works by repeatedly finding the smallest (or largest) 
element in an unsorted array and swapping it with the first element of the unsorted array. 
The algorithm repeatedly finds the smallest (or largest) element in the unsorted portion of the array 
and swaps it with the first element of the unsorted part. 
This process is repeated for the remaining unsorted portion until the entire list is sorted.

Selection sort is a very simple algorithm to understand and implement. 
However, it is not very efficient. The worst-case time complexity of selection sort is O(n^2), 
where n is the number of elements in the array. 
This means that the time it takes to sort the array grows quadratically with the number of elements.

Selection sort is often used as a teaching example for sorting algorithms. 
It is also sometimes used to sort small arrays, where the performance of the algorithm is not as important.

"""
def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1,len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i],array[min_index] = array[min_index],array[i]
    return array


array = [10, 5, 2, 7, 3, 1, 8, 9, 6]

print(selection_sort(array))