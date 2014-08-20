"""Friday 9th May 2014
Itumeleng Nqoko
Assignment 8 question 2"""
#Program to count pairs of repeated characters within a string
message=input("Enter a message:\n")
print("Number of pairs: ",end="")


def countpairs(message,counter):
    if len(message)==0 or len(message)==1:
        return counter
    else:
        if message[0]!=message[1]:
            return countpairs(message[2:],counter)
        else:
            counter+=1
            return countpairs(message[2:],counter)
print(countpairs(message,0))
    
       

