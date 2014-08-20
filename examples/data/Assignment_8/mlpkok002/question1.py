def palindrome(s):
    #base case
    if len(s)==0 or len(s)==1: 
        return "Palindrome!"
    
    #recursive step
    else: #if the length of the string (parameter) is greater than 1:
        if s[0]==s[-1]: 
            return palindrome(s[1:-1])
        else:
            return "Not a palindrome!"   #if the length of the string (parameter) is greater  than 1, return "Not a palindrome" and end.   
        
#line 3: if the string (the parameter) that the function is called with has a length of 0 or a length of 1, the string (paramter) is a palindrome, return "Palindrome" and end.       
#line 8-9: if the first and last characters of the string are the same, call the function again (with a different parameter): now with the string sliced such that the the two characters that were compared in the previous "call" of the function are removed. This will be done (if the successive parameters keep satisfying the condition) until the function is called with a parameter (string) such that the length of the string equals 0 or equals 1, where the function returns "Palindrome" and ends.    
        
s=input("Enter a string:\n")
print(palindrome(s))
        
      
        
    