"""Program to Count the Number of Pairs of Repeated Characters in a String Using Recursion
Tamsin Kantor
May 2014"""

def count_pairs(s):
    if s == "" or len(s) == 1: # base case to end recursion 
        return 0
    elif s[0] == s[1]: # if a pair is found
        return 1 + count_pairs(s[2:len(s)])  
    else: # if a pair is not found
        return count_pairs(s[1:len(s)])
    
string = input ("Enter a message:\n") #run function
answer = count_pairs(string)
print("Number of pairs:", answer) # print the output