
def anagram(string1, string2):  
    dct = {}
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string1[i] in dct.keys():
            var = dct[string1[i]] + 1
            dct[string1[i]] = var
        else:
            dct[string1[i]] = 1
  
    for j in range(len(string2)):
        if string2[j] in dct.keys():
            dct[string2[j]] -= 1
            if dct[string2[j]] == 0:
                del dct[string2[j]] 
        else:
            return False
    
   
    return not (bool(dct))

str1 = 'bool'
str2 = 'boll'

anagram_word = anagram(str1, str2)

print(anagram_word)

s1 = 'word'
s2 = 'dwro'

word_anagram = anagram(s1, s2)
print(word_anagram)



 
 
