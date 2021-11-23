def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        # i is the index in the list
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
            # else:
            #     min_index += 1
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print(selection_sort([4, 2, 6, 8, 1, 5]))
