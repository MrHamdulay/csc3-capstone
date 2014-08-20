# program that uses a recursive function to count the 
# number of pairs of repeated characters in a string
# Michele Balestra  BLSMIC004
# 6 May 2014


def pairs(string):
    '''function determines how many pairs in string'''
    if len(string)<2:
        return 0 
    if string[0] == string[1]:
        return 1 + pairs(string[2:])
    else:
        return pairs(string[1:])
    
if __name__=='__main__':
    msg = input('Enter a message:\n')
    print('Number of pairs:', pairs(msg))