#Mbongeni Mazibuko
#MZBMBO002
#Assignment 8

count=0
def pairs(s):
    '''recursive function to count the number of pairs of repeated characters in a string'''
    global count
    '''variable defined out of function'''
    if len(s)<2:
        print('Number of pairs:', count)
    elif s[0]==s[1]:
        count+=1
        return s[0]==s[1] and pairs(s[2:])
    else: return pairs(s[2:])
    
s=input('Enter a message:\n')
pairs(s)