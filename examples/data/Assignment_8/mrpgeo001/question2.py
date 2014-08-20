"""Program to count the number of repeated chracters in a string
Geoff Murphy
MRPGEO001
8 May 2014"""

string = input("Enter a message:\n")

counter = 0

def pair_check(string):
    global counter                              #Allows the counter variable to be used in and out of the function  
    if len(string) == 0 or len(string) == 1:    #Base case: If the string length is 0 or 1
        return counter
    
    elif string[0] == string[1]:                #Adds one to the counter if the 1st and 2nd letters are the same
        counter += 1
        return pair_check(string[2:])           #Recursive Step: Returns to the function again from the third letter onwards
    
    elif string[0] != string[1]:                #Runs the recursive step only if the 1st and 2nd letters are not the same
        return pair_check(string[2:])
    
pair_check(string)

print("Number of pairs:", counter)