"""katlego gaveni 7th may 2014"""
"""programme that counts the number of pairs of letters in a string recursively"""

def count(s):
    
    
    if s[0]==" ": #if the first letter is a space skip this letter and run the function from the second letter
        return count(s[1:])
    elif len(s)==1:# if the length of the string is 1 then they are no pairs
        return 0
    
    elif len(s)==2:
        if s[0]==s[1]:
            return 1
        else:
            return 0
    
    else:
        if s[0]==s[1]: #if the letters are the same the function counts and runs the function recursively from position 2 of the string
            return 1 + count(s[2:])
        
        else:
            return 0 + count(s[1:]) #if the letters are not the same the function adds 0 to the count and runs the function recursively from position 2 of the string
        
if __name__=='__main__':
    s=input("Enter a message:\n")#input from user
    print("Number of pairs:",count(s))      
    
           