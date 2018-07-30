def find_minimum(list_of_integers):
  """
  Given a list of integers, find the minimum number from that list.
  """
  
  smallest = list[0]

  for i in range(1, len(list)):
    if list[i] < smallest:
      smallest = list[i] 
     
  return smallest 
  
list_of_ints = [6, 5, 7, 3, 9, 2, 9, 9, 6, 1, 9, 7]
minimum = find_minimum(list_of_ints)