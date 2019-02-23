def multiples(lst):
    """
    Go through a list of 100 numbers and 
    print "buzz" if the number is a multiple of 3
    print "fizz" if the number is a multiple of 5
    print "buzzfizz" if the number is a multiple of both 3 and 5
    """
    for num in range(lst):
        if num % 3 == 0:
            print("buzz")
        if num % 5 == 0:
            print("fizz")
        if num % 3 == 0 and num % 5 == 0:
            print("buzzfizz")
        