list_numbers = [1, 3, 4, 2, 6, 5, 8, 7, 9, 10, 14, 13, 20, 21, 17, 15, 19]


def sort(lst):
  for i in range(len(lst) - 1):
    for i in range(len(lst) - 1 - i):
      if lst[i + 1] < lst[i]:
        temp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = temp

  return lst
  
sort(list_numbers)
