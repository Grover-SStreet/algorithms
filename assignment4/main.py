def tuple_partition(array, start, end):
    pivot = array[end][1]
    element_pointer = start - 1
    for j in range(start, end):
        if pivot == array[j][1]:
            pivot = str(array[end][0])[:1]
            if str(array[j][0])[:1] <= pivot:
                element_pointer += 1
                (array[element_pointer], array[j]) = (array[j], array[element_pointer])
            pivot = array[end][1]
        else:
            if array[j][1] > pivot:
                element_pointer += 1
                (array[element_pointer], array[j]) = (array[j], array[element_pointer])
    (array[element_pointer + 1], array[end]) = (array[end], array[element_pointer + 1])
    return element_pointer + 1


def sort_tuples(temp_array, temp_start, temp_end):
    if temp_start < temp_end:
        pivot_element = tuple_partition(temp_array, temp_start, temp_end)
        sort_tuples(temp_array, temp_start, pivot_element - 1)
        sort_tuples(temp_array, pivot_element + 1, temp_end)

# test case 1
arr = [("apple", 5), ("orange", 3), ("banana", 5), ("grape", 1), ("cherry", 3)]
sort_tuples(arr, 0, len(arr) - 1)
assert arr == [("apple", 5), ("banana", 5), ("cherry", 3), ("orange", 3), ("grape", 1)]

# test case 2
arr = [("apple", 5), ("orange", 3), ("banana", 5), ("grape", 1), ("cherry", 3), ("pear", 2), ("kiwi", 2),
       ("pineapple", 7), ("mango", 1), ("melon", 7)]
sort_tuples(arr, 0, len(arr) - 1)
assert arr == [("melon", 7), ("pineapple", 7), ("apple", 5), ("banana", 5), ("cherry", 3), ("orange", 3), ("kiwi", 2),
               ("pear", 2), ("grape", 1), ("mango", 1)]

# test case 3
arr = [("x", 10), ("a", 10), ("c", 20), ("b", 20), ("d", 5), ("e", 5), ("g", 15), ("f", 15), ("h", 5), ("i", 5)]
sort_tuples(arr, 0, len(arr) - 1)
assert arr == [("b", 20), ("c", 20), ("f", 15), ("g", 15), ("a", 10), ("x", 10), ("d", 5), ("e", 5), ("h", 5), ("i", 5)]

# test case 4
arr = [("laptop", 7), ("monitor", 5), ("keyboard", 3), ("mouse", 3), ("printer", 4), ("headset", 4), ("webcam", 2),
       ("microphone", 1), ("speaker", 6), ("charger", 6)]
sort_tuples(arr, 0, len(arr) - 1)
assert arr == [("laptop", 7), ("charger", 6), ("speaker", 6), ("monitor", 5), ("headset", 4), ("printer", 4),
               ("keyboard", 3), ("mouse", 3), ("webcam", 2), ("microphone", 1)]
