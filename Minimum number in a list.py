def find_minimum(list_of_integers):
  """
  Given a list of integers, find the minimum number from that list.
  >>> list_of_ints = [6, 5, 7, 3, 9, 2, 9, 9, 6, 1, 9, 7]
  >>> find_minimum(list_of_ints)
  >>> 1
  """
  
  smallest = list_of_ints[0]

  for i in range(1, len(list_of_ints)):
    if list_of_ints[i] < smallest:
      smallest = list_of_ints[i] 
     
  return smallest 