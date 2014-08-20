'''program to count recursively the number of pairs of repeated non-overlapping characters in a string
tom new
2014/05/05'''

def pairs (s):
    '''counts pairs of... things...'''
    if len (s) == 1 or len (s) == 0: return 0 # end point (0 copes with the empty string, otherwise ends at 1)
    elif s [0] == s [1]: return 1 + pairs (s [2:]) # if first 2 characters are the same sends rest of string to pairs ( )
    else: return pairs (s [1:]) # sends the string minus the first character to pairs ( )

# gets input from user if program is run directly
if __name__ == '__main__':
    s = input ('Enter a message:\n')
    print ('Number of pairs:', pairs (s))