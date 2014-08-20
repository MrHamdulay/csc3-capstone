"""recursively counts number of pairs of repeated characters in a string
jonathan nathan
7 may 2014"""

def count_pairs(string):
    """counts pairs in string"""
    # base case for when a string has 1 or no characters in it
    if len(string) < 2:
        return 0
    # checks whether the first two characters are identical
    elif string[0] == string[1]:
        # recurses with the first two characters of the string removed (to avoid overlapping)
        return count_pairs(string[2:]) + 1
    else:   
        # recurses with the first character of the string removed
        return count_pairs(string[1:])
        
    
# gets input from user
string = input('Enter a message:\n')
# prints result from count_pairs function	
print('Number of pairs:', count_pairs(string)) 


    