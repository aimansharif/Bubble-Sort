def count_items(list, target):
  
  count = 0
  
  for element in list:
    if element == target:
      count = count + 1
      
  return count 
      
lists_of_ints = [1, 5, 7, 3, 9, 2, 9, 9, 6, 4, 9, 1]
x = 9
count = count_items(lists_of_ints, x)
