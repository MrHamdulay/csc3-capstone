"""program to count the number of pairs in a string
yasha longstaff 
6 may 2014"""


def pairs(s):
    if len(s) >=2: #must be more than 2 characters in the string
        if s[0] != s[1]: #first 2 letters aren't equal
            return pairs(s[1:]) #check the rest of the word with the fuction
        else: #first 2 letters are the same
            return 1 + pairs(s[2:]) #count 1 and then repeat function
    else: #less than 2 characters in string
        return 0
                             
s = input('Enter a message:\n')
print('Number of pairs:', pairs(s))
