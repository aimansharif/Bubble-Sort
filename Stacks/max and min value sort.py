lst = [3, 4, -2, 6, -5, 8, 7, 9, 10, 14, -13, 1, 40, 20, 21, -25, 15, 19]

#finding the maximum value from a list of numbers

def max_value(number_list):
    max_value = lst[0]
    for i in range(0, (len(lst) - 1)):
        if lst[i] > max_value:
            max_value = lst[i]
            
    return max_value

#finding the minimum value from a list of numbers

def min_value(number_list):
    min_value = lst[0]
    for i in range(0, (len(lst) - 1)):
        if lst[i] < min_value:
            min_value = lst[i]
            
    return min_value