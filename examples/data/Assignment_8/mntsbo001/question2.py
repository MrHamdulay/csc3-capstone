"""Program to count number of pairs
Sbonelo Mntungwa
9 May 2014"""

def pairs(string,count):                    #Defining function pairs
    if len(string) <2:                      #When the length of the string is less than two
        print("Number of pairs:",count)     #Printing out the final output
    elif string[0] == string[1]:            #Checking if the first character is the same as the second character
        return pairs(string[2:],count+1)    #Repeating function where the string begins on third character, adding count by one
    
    else:
        return pairs(string[1:],count)      #Returning function beginning with second character
    
string=input("Enter a message:\n")          #Inputing string
count = 0                                   #Assigning count
pairs(string,count)                         #running the function pairs
    