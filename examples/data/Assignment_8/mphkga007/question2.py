"""number of pairs in a string
kenneth mphele
6 may 2014"""
count=0
def pairs(s):
    global count
    message="Number of pairs:"
    # checks if there are enough characters to compare
    if len(s)==0 or len(s)==1:
        return message+" "+str(count)
    #checks if consecutive characters are the same or not
    else:
        if s[0]==s[1]:
            count+=1 #counts how many pairs
            return pairs(s[2:])
        # calls the function again if consecutive characters are not the same
        else:
            return(pairs(s[1:]))


s=input("Enter a message:\n")
print(pairs(s))