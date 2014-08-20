#counts the number of pairs of letters in an input string
#By Chloe Longmore
# 5 May 2014

message=input("Enter a message:\n")

def check_pairs(message):
    #base-case when the string is empty
    if message=='':
        return 0
    # checks if the first two letters are the same   
    elif message[:1]==message[1:2]:
        #slices first two letters off the string
        message=message[2:]
        #recursion
        return 1 + check_pairs(message)
    #if first two letters are not the same    
    elif message[:1]!=message[1:2]:
        #slices first letter off the string
        message=message[1:]
        #recursion
        return check_pairs(message)

check_pairs(message)
print("Number of pairs:",check_pairs(message))