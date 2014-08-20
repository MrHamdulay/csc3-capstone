"""recursive function to count the number of pairs of repeated characters in a string
joshua wort
5 May 2014"""

def pairs(string):
    #base case
    if len(string)<=1:
        return 0
    #check if the very first two characters in the string are the same and repeat process
    elif string[0]==string[1]:
        return 1 + pairs(string[2:]) #if first two characters equal counter adds 1
    else:
        return pairs(string[1:])
    
message = input("Enter a message:\n")
print("Number of pairs:", pairs(message))