
def bubble_sort(mylist):
    """ The Bubble Sort looks at pairs of adjacent elements in an array, 
    one pair at a time, and swap their positions if the first element is 
    larger than the second, or simply move on if it isn't. """
    for i in range(len(mylist) - 1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j + 1]:
                temp = mylist[j]
                print(f"PRINTING TEMP: {temp}")
                mylist[j] = mylist[j + 1]
                mylist[j + 1] = temp 
    return mylist

print(bubble_sort([1,3,2,9,2,4]))



def selection_sort(mylist):
    """The Selection Sort selects the smallest element from an unsorted list in each iteration
    and places that element at the beginning of the unsorted list."""
    for i in range(len(mylist) - 1):
        min_index = i 
        for j in range(i + 1,len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j
        if i != min_index:
            temp = mylist[i]
            mylist[i] = mylist[min_index]
            mylist[min_index] = temp 
    return mylist 

print(selection_sort([1,3,2,9,2,4]))


