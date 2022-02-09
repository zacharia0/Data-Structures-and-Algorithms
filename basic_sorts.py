
def bubble_sort(my_list):
    """ The Bubble Sort looks at pairs of adjacent elements in an array, 
    one pair at a time, and swap their positions if the first element is 
    larger than the second, or simply move on if it isn't. """
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                print(f"PRINTING TEMP: {temp}")
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp 
    return my_list

print(bubble_sort([1,3,2,9,2,4]))



def selection_sort(my_list):
    """The Selection Sort selects the smallest element from an unsorted list in each iteration
    and places that element at the beginning of the unsorted list."""
    for i in range(len(my_list) - 1):
        min_index = i 
        for j in range(i + 1,len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp 
    return my_list 

print(selection_sort([1,3,2,9,2,4]))


def insertion_sort(my_list):
    """The Insertion Sort assumes that the first card is already sorted then,
     it selects an unsorted card. if the unsorted card is greater than the 
     card in hand, it is placed on the right otherwise, to the left. In the same way,
      other unsorted cards are taken and put in their right place. """

    for i in range(1,len(my_list)):
        temp = my_list[i]
        j = i - 1 
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([1,3,2,9,2,4]))



