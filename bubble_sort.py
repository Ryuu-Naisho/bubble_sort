'''
Time Complexity best, average, worst -> O(n), O(n^2), O(n^2)
Space Complexity O(1)
Sort a sequence of numbers. Compares values from the right end, if the value on the right is smaller then the value on the left, the values will be swapped until they're all sorted.
'''


def bubble_sort(sequence):
    size = len(sequence)
    

    for i in range(size - 1):
        for j in range(size-i-1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]



    return sequence



unsorted_array = [64,34,25,12,22,11,90]
sorted_array = bubble_sort(unsorted_array)

for i in range(len(sorted_array)):
    print(sorted_array[i], end=' ')
print()
