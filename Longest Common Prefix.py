def longestCommonPrefix(lst):
    """
    :type strs: List[str]
    :return type: str
    """
    if lst == []:
        return ""
    
    min_word = min(lst)
    temp_word = lst[0]
    lst[lst.index(min_word)] = temp_word
    lst[0] = min_word

    string = ""

    for i in range(0,len(min_word)):
        for j in range(1, len(lst)):
            if lst[0][i] != lst[j][i]:
                return string
        string += lst[0][i]

    return string