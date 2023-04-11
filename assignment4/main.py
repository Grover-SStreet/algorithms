def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(temp_array):
    length_of_array = len(temp_array)

    for i in range(length_of_array // 2, -1, -1):
        heapify(temp_array, length_of_array, i)

    for index in range(length_of_array - 1, 0, -1):
        # Swap
        temp_array[index], temp_array[0] = temp_array[0], temp_array[index]
        heapify(temp_array, index, 0)


arr = [1, 12, 9, 5, 6, 10]
heap_sort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')
