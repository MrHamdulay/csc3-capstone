#HLNCEC001
#Question2
#Assignment8
#Recursion for counting the number of pair of words.

c=0
def Pairs(s):
    global c
    s = s.split()
    s = ''.join(s)
    if len(s) == 1:
        print("Number of pairs:",c//2)
    elif s[0] in s[1:]:
        c+=1
        return Pairs(s[1:])
    else:
        return Pairs(s[1:])
            
Pairs(s=input('Enter a message:\n'))