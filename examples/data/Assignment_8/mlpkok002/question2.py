def countpairs (s): 
    #base case
    if len(s)==1 or s=="": #if the length of the string (parameter) that the function is called with has a length of 1 or is an empty space (at the end of a string), return 0 (since there can be no matches if there is only one character or empty space) and end.
            return 0
    #recursive step 1
    elif s[0] == s[1]:
        return 1 + countpairs (s[2:])
    #recursive step 2
    else:
        return countpairs (s[2:])
    
# recursive step 1: if the first and second characters of the parameter/string are the same, call the function again (with a different parameter): now with the parameter/string sliced such that the two characters that were compared in the previous call of the function are removed. This will be done  (if the successive (smaller) parameters/strings KEEP SATISFYING THE CONDITION), where 1 keeps being added, until the function is called with a parameter/string such that the length of the parameter/string equals 0 or there is nothing left of the string, where it returns 0, adding it to the 1 (or cumulative amount) (line 7) and ends, or if the parameter (the sliced string) that the function is called with does not satisfy the condition, the function is called again (recursive step 2) until the string is sliced such that 1 character or none is left, the function returns 0 (adding it to whatever cumulative amount) and ends.

s=input("Enter a message:\n")
print("Number of pairs:",countpairs(s))