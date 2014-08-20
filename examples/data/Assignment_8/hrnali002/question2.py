"""A recursive program to count the number of pairs of repeated characters in a string
Alison Hoernle
HRNALI002
4 May 2014"""

def pairs(string):
    
    count = 0

    # Base case
    if len(string) <= 1:
        return count
    
    else:
        
        if string[-1] == string[-2]:
            count += 1
            string = string[0:-1]
        
        return count + pairs(string[0:-1])
  
string = input("Enter a message:\n")
pairs = pairs(string)
print("Number of pairs:", pairs)    
    
    