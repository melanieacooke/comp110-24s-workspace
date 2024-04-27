"""Functions that implement sorting algorithms."""

__author__ = "730529937"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    i: int = 0
    while i < len(x):
        # Find the index of the minimum element in the unsorted portion
        min_index: int = i
        j: int = i + 1
        while j < len(x):
            if x[j] < x[min_index]:
                min_index = j
            j += 1
        # Swap the minimum element with the current element
        x[i], x[min_index] = x[min_index], x[i]
        i += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    i: int = 1
    while i < len(x):
        #Track the unsorted index
        unsorted_index: int = i
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index - 1]:
            #Swap the current element for the one before it
            x[unsorted_index], x[unsorted_index - 1] = x[unsorted_index - 1], x[unsorted_index]
            #Decrement the unsorted index
            unsorted_index -= 1
        i += 1
    return None
    