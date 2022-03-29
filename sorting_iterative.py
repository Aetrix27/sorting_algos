#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    """Average O(n) Best O(1)"""

    isSorted = True
    for idx, val in enumerate(items, start = 1):
        first_num = idx-1
        second_num = idx
        if second_num > first_num:
            isSorted = True
        else:
            return False

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) in average and worst case, O(n) best case
    TODO: Memory usage: ??? Why and under what conditions?
    Memory is O(n) because a new variable is assigned each time in the loop
    
    """
    
    #line 2 has -1 in it as well since once we get to  the last traversal, a singular element can’t be sorted any further

    for _ in range(len(items) - 1):
        for j in range(len(items) - 1 - _):

            if items[j]> items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items
        
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

print(bubble_sort([2,5,1,2,3]))


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: 
    TODO: Memory usage: ??? Why and under what conditions
    
    """
    
  
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
print(selection_sort([1,7,4,3,2]))

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n) when array is sorted or you only need to pass through one time and O(n)^2 for the average and best case
    TODO: Memory usage: O(n) """

    # [1,7,4,3,2 ]
    #  i   j

    # Traverse through 1 to len(arr)


print(insertion_sort([1,7,4,3,2]))       
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items