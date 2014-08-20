# a program that uses a recursive function to count the number of pairs of repeated characters in a stringme 
#Jenny Luo
# 9 May 2014

message=input("Enter a message:\n")


def count(message):
    if message!= "":
        if len(message)==1:# check to see if the length of the message is 1
            return 0
        if message[0]==message[1]:# check to see if the first charcater and the second character are the same, i.e. a pair
            message=message[2:]
            return 1+ count(message)#recursive statement
        
        else:
            message=message[1:]
            return count(message)#recursive statement
    else:
        return False


print("Number of pairs:",count(message))