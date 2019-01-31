import string

def build_dictionary(words):
  """
  Given a list of words, returns a dictionary with the length of each word as a key and the word as a value.
  Counts the number of letter in each word. 
  >>> word_list = ['the', 'the', 'the', 'hello', 'hi', 'hi', 'hi', 'in', 'world', 'world']
  >>> {5: ['world', 'hello'], 2: ['hi', 'in'], 3: ['the']}
  """
  
  word_set = set(words)
  dct = {}
  
  for word in word_set:
    word = word.strip(string.punctuation).lower()
    
    
    length = len(word)
    
    lst = dct.get(length, [])
    lst.append(word)
    dct[length] = lst 
  
  return dct 
  