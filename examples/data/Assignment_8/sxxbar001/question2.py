#Assignment 8
#Question 2
#Barry Su
#8 May 2014
#Program to count the number of pairs of repeated charac in string

#get string
string=input("Enter a message:\n")
count=0
def pairs(string):
    if len(string)<2:   #if string is less than 2 characs
        return 0        #return 0 because it is not a pair
    elif string[0]==string[1]:
        return 1+pairs(string[2:])  #if the first and sec charac are same, return 1 (no of pairs currently) and rest of string
    else:
        return 0+pairs(string[1:])  #if first and sec charac don't equal, return 0 (no. of pairs currently) and cut first charac off
    
print("Number of pairs:",pairs(string))
        
    
    