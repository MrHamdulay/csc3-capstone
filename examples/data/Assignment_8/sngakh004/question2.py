"""Program to count pairs of characters in a string.
Akhil Singh
SNGAKH004
7 May 2014"""

#Prompt user for string.
str1ng= input("Enter a message:\n")

#Defining a counter to keep track of the number of pairs of characters.
pair_counter = 0

def counting_pairs(str1ng):
    global pair_counter
    #Terminate once the length of the string analysed in the current recursion is 1 or 0.
    if len(str1ng) <= 1:
        print("Number of pairs:", pair_counter) 
    
    #If the first 2 characters in the string are the same, delete both and add 1 to the counter.    
    elif str1ng[0] == str1ng[1]:
            pair_counter += 1
            str1ng = str1ng[2:]
            return counting_pairs(str1ng) 
     
     #If the first 2 characters in the string are not the same, delete only the first one.   
    else:  
        str1ng = str1ng[1:]
        return counting_pairs(str1ng)        
    
if __name__=="__main__":
    counting_pairs(str1ng)