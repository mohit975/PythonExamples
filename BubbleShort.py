"""
Bubble sort is a simple sorting algorithm that works by repeatedly comparing adjacent elements in an array and swapping them if they are in the wrong order. 
The algorithm starts at the beginning of the array and compares the first two elements. 
If the first element is greater than the second element, the two elements are swapped. 
The algorithm then moves on to the next two elements and repeats the process. 
This continues until the algorithm reaches the end of the array.
Bubble sort is a very simple algorithm to understand and implement. 
However, it is not very efficient. The worst-case time complexity of bubble sort is O(n^2), 
where n is the number of elements in the array. This means that the time it takes to sort the array grows quadratically with the number of elements.

Bubble sort is often used as a teaching example for sorting algorithms. 
It is also sometimes used to sort small arrays, where the performance of the algorithm is not as important.

Here is an example of how bubble sort works:"""

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range (len(array) -i -1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
    return array


    print(array)

array = [10, 5, 2, 7, 3, 1, 8, 9, 6,10, 5, 2, 7, 3, 1, 8, 9, 6]

print(bubble_sort(array))