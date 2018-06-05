

Tahsin sharif

word 1 = bool
word 2 = boll

key -> value
b -> 1 - 1
o -> 2 - 1
l -> 1 - 2

b -> 1
o -> 1
l -> 2[]

dictionary after
b -> 0
o -> 1
l -> -1

for()
 //bool dictionary created
 arr1 = 'bool'
 
for()
 //for loop for boll
 arr = 'boll';

toon
oton
 
 //dictionary for ton
toon
oton

dict = {}
bool(dct)

 
 toyyu
 yuity 
 
 t -> 1
 o -> 1
 y -> 1
 u -> 0 
 
#word1 = 'boll'
#word2 = 'bool'

### case1: when key does not exist -> value = 1
### case2 : when key does exist -> value++

### bool   b = 1, o = 2, l = 1
### boll   


 def anagram(string1, string2):  
  dct = {}
  if len(string1) != len(string2):
  	return False
  
  for i in string1:
    if 'string1[i]' in dct.keys():
    	dct[string1[i]] += 1
    else:
    	dct[string1[i]] = 1
    
	for j in string2:
  	if 'string2[i]' in dct.keys():
    	dct[string[j]] -= 1
    	if dct[string[j]] == 0:
    		del dct[string[j]] 
    else:
    	return False
    
  return !bool(dct)
  
  
"""     
b -> 1
o -> 0
l -> 0

dct = {}
"""


 list1 = [23, 43, 12, 45, 60, 30]
 list2 = [1, 2, 3, 4]
 
 int size1 = (sizeof(list1)/sizeof(list1[0]));
 int size2 = (sizeof(list2)/sizeof(list2[0]))	
 int list3[size1 + size2];
 
 for(int i=0; i<size1; i++){
 	list3[i] = list1[i];
 }

/// size1 = 6
/// list3[] = {23,43,12,45,60,30, , , , };
 
 for(int i=0; i<size2; i++){
 	list3[i + size1] = list2[i];   // list2 = 0, list3 = 6 /// list2 = 1, list3 = 7 /// list2 = 2, list3 = 8
 }
 
 
 
 
