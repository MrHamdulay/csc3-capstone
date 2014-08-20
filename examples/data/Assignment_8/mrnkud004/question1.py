"""Check palindrome
kennedy muranda
8/5/2014"""

#define the function
def palind_check(string_entered):
    if len(string_entered)<2:
        return print("Palindrome!")
    
    else:
        if string_entered[0]==string_entered[-1]:
            return palind_check(string_entered[1:-1])
        #if string is not palindrome
        else:
            return print("Not a palindrome!")
        
string_entered = input ("Enter a string:\n")
palind_check(string_entered)
    
        