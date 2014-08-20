#Shivaan Motilal
#4 May 2014

string=input("Enter a string:\n")



def pal(string):
    
    if len(string)<2 :             #if less than 2 letters left, it has survived
        return "Palindrome!"
    else:
        if string[0]==string[-1]:     #if the first letter is equal to last letter
            string=string[1:-1]
            return pal(string)
        
        
        else:
            return "Not a palindrome!"
    
print(pal(string))