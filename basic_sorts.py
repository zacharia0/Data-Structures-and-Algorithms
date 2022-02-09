""" The Bubble Sort looks at pairs of adjacent elements in an array, 
one pair at a time, and swap their positions if the first element is 
larger than the second, or simply move on if it isn't. """
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j + 1]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp 
    return my_list