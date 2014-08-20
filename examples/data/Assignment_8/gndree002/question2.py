"""Recursive function to count the number of pairs of repeated characters in a string 
Reece Gounden
7 May 2014"""
string = input("Enter a message:\n")
strcnt = '' #string to store pairs char pairs


def cntPairs(string):
    global strcnt
    if len(string)>1:
        if string[0]==string[1]: #if 1st and 2nd letters match extracts those two letters match extracts those to letters and deletes them from string
            strcnt=strcnt+string[0:2]
            string=string[2::]
        else: #otherwise just deletes the first letter and checks again
            string=string[1::]
        cntPairs(string)

cntPairs(string)
cnt = int(len(strcnt)/2) #counts number of chars in strsnt and divides by two to get no. of strings
print("Number of pairs: "+str(cnt))