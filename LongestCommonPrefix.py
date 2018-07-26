def longestCommonPrefix(lst):
    """
    >>> ["flower","flow","flight"]
    >>> fl
    """
    length_lst = len(lst)
    
    for i in range(length_lst):
        length_word = len(lst[i])
        
        if length_word == 1:
            if lst[i][0] == lst[i+1][0]:
                return lst[i][0]
        
        for j in range(length_word):
            if(lst[i][j] + lst[i][j+1]) == (lst[i+1][j] + lst[i+1][j+1]):
                return lst[i][j] + lst[i][j+1]
        
            else:
                return ""
