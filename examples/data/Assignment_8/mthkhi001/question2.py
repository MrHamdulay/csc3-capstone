#Recursion
#MTHKHI001
#Assignment 8
#question 2

"""program designed to test the number of repeated (ie adjacent same letter) character in a string, pairs of chars cant overlap"""


def count_pairs(message,length,position,counter):
    #print(str(position))
    #print(str(length))
    if  position >= length-1:
        #print(str(position))
        return counter
    
    else:
       # print(message[position -1])
       # print(message[position])
       # print(message[position + 1])
        if message[position] == message[position+1]:
            return count_pairs(message,length,(position+2),(counter+1))
        else:
            return count_pairs(message,length,(position+1),counter)
                

message = input("Enter a message:\n")
counter = 0
length = len(message)

position = 0

total = count_pairs(message,length,position,counter)

print("Number of pairs: " + str(total))


        
    
    


