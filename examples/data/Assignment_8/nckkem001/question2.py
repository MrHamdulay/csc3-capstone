"""Program to count pairs of characters in a string.
Kemeshan Naicker
7 May 2014"""

#Prompt user for string.
string = input("Enter a message:\n")

#Define a counter to keep track of the number of pairs of characters.
pair_count = 0

def count_pairs(string):
    global pair_count
    #Design recursion to terminate once the length of the string analysed in the current recursion 1 or 0.
    if len(string) <= 1:
        print("Number of pairs:", pair_count)
    
    #If the first 2 characters in the string are the same, delete both and add 1 to the counter.        
    elif string[0] == string[1]:
        pair_count += 1
        string = string[2:]
        return count_pairs(string)
    
    #If the first 2 characters in the string are not the same, delete only the first one.    
    else:
        string = string[1:]
        return count_pairs(string)
    
if __name__=="__main__":
    count_pairs(string)
    
                            