def max_value(list_of_ints):
  """
  Given a list of integers, find the maximum value from the list. 
  >>> lst = [2, 5, 10, 8, 25, 9, 7]
  >>> max_value(lst)
  >>> 25
  """
  
  i = 0 
  max_value = list_of_ints[0] 
  
  for number in list_of_ints:
    if number > max_value:
      max_value = list_of_ints[i]
    i += 1
    
  return max_value
  