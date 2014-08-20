"""blessings hadebe
count number of pairs in a given string #question2.py 
9 may 2014"""

#count number of pairs in a given string
def countPairs(string): 
    global count
    if len(string) <2:
        return "Number of pairs: " + str(count)
    else:
        if (ord(string[0])) != ord(string[1]):
            return countPairs(string[1:])
        else:
            count+=1
            return countPairs(string[2:])
count=0
string=input("Enter a message:\n")
print(countPairs(string))