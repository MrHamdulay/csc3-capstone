def count(s): 
    if len(s) > 1: 
        if s[0] == s[1]: 
            return 1 + count(s[2:]) 
        else: 
            return count(s[1:]) 
    else:
        return 0 
    
    
string = input("Enter a message:\n")
pair = count(string)
print("Number of pairs:", pair)

