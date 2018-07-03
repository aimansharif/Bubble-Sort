def isPalindrome(number):
    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
    
    >>> isPalindrome(121)
    >>> True
    >>> isPalindrome(1231)
    >>> False
    
    """
    string = str(n)
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    if reversed_string == string:
        return True
    else:
        return False