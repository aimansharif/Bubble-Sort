def count_items(lst, target):
  """
  Given a list, count the number of occurences of target in the list.
  >>> lists_of_ints = [1, 5, 7, 3, 9, 2, 9, 9, 6, 4, 9, 1]
  >>> target = 9
  >>> count_items(lists_of_ints, x)
  >>> 4
  """
  count = 0
  
  for element in list:
    if element == target:
      count = count + 1
      
  return count 