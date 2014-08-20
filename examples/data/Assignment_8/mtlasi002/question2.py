#Asil Motala
#MTLASI002
#Assignment 8
#Question 2
#27 April 2014

def count_pairs(message):
    if len(message)==1:                         #breaking condition if only one unit left in string
        return 0
    elif message[0]==message[1]:                #check if adjacent letters are same
        if len(message)==2:
            return 1                            #add 1 to count for end of string
        else:
            return 1 + count_pairs(message[2:]) #add 1 to count and continue to check rest of string
    else:
        return count_pairs(message[1:])         #check for next set of letters without adding anything

message=input("Enter a message:\n")             #get input from user
print("Number of pairs:",count_pairs(message))  #print result