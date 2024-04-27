"""List Utils."""

__author__ = "730529937"


def all(lst: list[int], num: int) -> bool:
    """Given an integer in a list, checks if all other integers are the same."""
    if not lst:
        return False  # If the list is empty, return False
        
    for item in lst:
        if item != num:
            return False  # If any item doesn't match the given number, return False
    
    return True 


def max(input: list[int]) -> int:
    """Looks at the maximum number in an input."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_num = input[0]
    for num in input:
        if num > max_num:
            max_num = num
    
    return max_num


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Checks to see if list length is equal."""
    if len(lst1) != len(lst2):
        return False  # If the lengths are different, lists cannot be equal
    
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False  # If any elements at corresponding indices are not equal, lists are not equal
    
    return True 


def extend(lst1: list[int], lst2: list[int]) -> None:
    """Given two lists of int values, mutate the first list of int values by appending the second lists values to the end of it."""
    for num in lst2:
        lst1.append(num)