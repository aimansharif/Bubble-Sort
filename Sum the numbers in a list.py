def sum_list(lst):
    
    """ 
    (list of number) -> number 
    
    Given a list of numbers, return the sum of the elements in list lst.
    >>> list_of_ints = [1, 5, 2, -4, 9, 3]
    >>> sum_list(list_of_ints)
    >>> 16
    """
    
    sum = 0
    for elem in lst:
        sum = sum + elem
    return sum              

#Python's built-in sum function does the same thing as sum_list
sum(list_of_ints)
