# IF List is almost sorted, I.S is O(N) and not O(N^2)
# Else all of the sorting algorithms are O(N^2)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([2, 6, 8, 1, 3, 4]))
