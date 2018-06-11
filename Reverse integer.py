def reverse(n):

    if n < 0:
        n = n * -1
        boolean = True
    else:
        boolean = False
    
    final_num = 0
    while n != 0:
        num = n % 10		
        length = len(str(n))		
        n = n // 10				
        final_num += num * (10 ** (length - 1))     
    
    if final_num > 2**31 - 1:
        return 0
    if boolean == True:
        final_num = -final_num
    
    return final_num