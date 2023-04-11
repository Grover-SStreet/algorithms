def merge_sort(array):
    single_element = 1
    if len(array) > single_element:
        array_middle = len(array) // 2
        left_split = array[:array_middle]
        right_split = array[array_middle:]

        merge_sort(left_split)
        merge_sort(right_split)

        index_one = 0
        index_two = 0
        index_three = 0

        while index_one < len(left_split) and index_two < len(right_split):
            if left_split[index_one] < right_split[index_two]:
                array[index_three] = left_split[index_one]
                index_one += 1
            else:
                array[index_three] = right_split[index_two]
                index_two += 1
            index_three += 1

        while index_one < len(left_split):
            array[index_three] = left_split[index_one]
            index_one += 1
            index_three += 1

        while index_two < len(right_split):
            array[index_three] = right_split[index_two]
            index_two += 1
            index_three += 1


arr = [3, 6, 1, 9, 5, 2, 4, 7, 8]
merge_sort(arr)
assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
