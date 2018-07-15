def romanToInt(s):
    """
    Given a Roman numeral, convert it to an integer.
    
    """
    dct = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    number = 0
    length = len(s)
    for i in range(length - 1):
        if dct[s[i]] < dct[s[i+1]]:
            number = number - dct[s[i]]
        else:
            number = number + dct[s[i]]

    number += dct[s[-1]]
    
    return number  