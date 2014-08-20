# Recursion
# Counting the number of pairs of repeated characters in a string
# Hendrik Joosten
# JSJOH004
# 04 May 2014

#check to seee that amount of pairs of chars exist in a word
def checkPairs(s,i):
    # base case when the len of the string is 1 or less
    # there cannot be any pairs left to check
    if len(s) <= 1:
        print("Number of pairs:",i)  
    # if the char is == to its adjacent char return the string minus those two chars
    elif s[0] == s[1]:
        #iterate the counter of amount of pairs
        i+=1
        return checkPairs(s[2:],i)
    #after a char is checked and it is != to its adjacent char
    # return and check the string from after that char
    else:
        return checkPairs(s[1:],i)
    
user_str_in = input("Enter a message:\n")
checkPairs(user_str_in,0)