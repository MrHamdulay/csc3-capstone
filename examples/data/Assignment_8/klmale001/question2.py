"""Counting program for strings
Alexi Kalamoudacos
8 May 2014"""

#Ask user for text
x = input("Enter a message:\n")

#count the number of pairs of characters
pair_count = 0

def count_pairs(x):
    global pair_count
    #end recursion once length is 1 or 0
    if len(x) <= 1:
        print("Number of pairs:", pair_count)
    
    #If the intial 2 letters in the string are identical, remove both and add 1 to the counter.        
    elif x[0] == x[1]:
        pair_count += 1
        x = x[2:]
        return count_pairs(x)
    
    #If the initial 2 letters in the string are not identical, delete only the first one.    
    else:
        x = x[1:]
        return count_pairs(x)
    
if __name__=="__main__":
    count_pairs(x)
    
                            