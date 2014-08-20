"""Counts number of repeated pairs of letters in a phrase
Trevor Byaruhanga
08 May 2014"""


def replace ( s, source, dest ):
    """replace all occurrences of source is s with dest"""
    # base case - no match possible
    if len (s) < len (source):
        return s
    # first recursive step - found the , so replaces it with an empty string
    elif s[:len(source)] == source:
        return dest + replace (s[len(source):], source, dest)
    # second recursive step - didnt find the comma so kept searching through the rest of the string until there are no more.
    else:
        return s[0] + replace (s[1:], source, dest)



       
def count(words):
    """Counts the number of repeated pairs od letters"""
    #base case, if its an empty string return 0.
    if words=='':
        return 0
    #second base case, if the length of the string is 1 return 0.
    elif len(words)==1:
        return 0
    #if the first letter is equal to the second, increase the number of pairs by one and search through the rest of the string for other pairs 
    elif words[0] == words[1]:
        return  1 +count(words[2:])
    #if not search through the rest of the string for other pairs starting from the next value(eg:- if 1st!=2nd start from 2nd.
    else:
        return 0 + count(words[1:])
    
  




message=input('Enter a message:\n')   
print('Number of pairs: ',end='')   
print(count((replace(message,',',''))))
          