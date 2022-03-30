#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: Average O(n), need to iterate through the list
    Memory usage: Best O(1), memory does not depend on input size.
    """ 

    isSorted = True
    if items == [] or len(items)==1:
        return isSorted
    for idx in range(len(items)-1):
        first_num = items[idx]
        second_num = items[idx+1]
        if second_num > first_num:
            isSorted = True
        else:
            isSorted = False
            return isSorted
    return isSorted
print(is_sorted(['D', 'A', 'C']))

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) in average and worst case, O(n) best case where numbers are already sorted
    Memory is O(1) because the array sorted in place and no extra memory is used.
    
    """
    
    #Subtract one in the last traversal, since a singular element can’t be sorted any further

    for _ in range(len(items) - 1):
        for j in range(len(items) - 1 - _):
            #Swap the adjacent items that are out of order
            if items[j]> items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

print(bubble_sort([2,5,1,2,3]))


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) average and worst cases, since it must past through the array twice.
    Memory usage: O(1) since the memory does not depend on input size.
    
    """
    
    for i in range(len(items)):
        min = i
        #Find min item in unsorted items in the rest of the unsorted array
        for j in range(i+1, len(items)):
            if items[min] > items[j]:
                min = j
                
        # Swaps it with the first unsorted item in finds
        items[i], items[min] = items[min], items[i]
    return items

print(selection_sort([1,7,4,3,2]))

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n) when array is sorted or you only need to pass through one time and O(n)^2 for the average and best case
    Memory usage: O(1) since memory does not depend on the input size.
    """

    # [1,7,4,3,2 ]
    #  i   j
    #Repeat until all items are in sorted order
    for i in range(1, len(items)):
        pivot = items[i]
 
        #Go through items before pivot
        j = i-1
        while j >= 0 and pivot < items[j]:
            #If a previous value is greater, swap it to put it in sorted order
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
            j -= 1

        
    return items

print(insertion_sort([1,7,4,3,2]))       
