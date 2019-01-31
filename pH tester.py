def pH_meter():
  """
  Given a pH value, check whether it is acidic or alkaline.
  """
  
  while True:
    ph = float(input('Enter the pH level: '))
  
    if ph < 7.0:
      print(ph, "is acidic\n")
    else:
      print(ph, "is alkaline\n")