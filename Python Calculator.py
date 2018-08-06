def calculator():

  while True:
    
    response = input("\nEnter an action(+, -, /, *): ")
    
    num1 = int(input("Input a number: ")) 
    num2 = int(input("Enter another number: "))
    
    if response == '+':
      print("The sum of", num1, "and", num2, "is", num1 + num2)
    elif response == "-":
      print("The subtraction of", num1, "and", num2, "is", num1 - num2)
    elif response == '/':
      print("The quotient of", num1, "and", num2,"is", num1 / num2)
    elif response == '*':
      print("The product of", num1, "and", num2, "is", num1 * num2)
    else:
      print("Invalid operator.")
    
    response = input("Continue? y/n: ")
    if response == 'y':
      continue
    else:
      return  