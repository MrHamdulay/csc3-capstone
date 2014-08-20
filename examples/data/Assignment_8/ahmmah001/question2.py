'''Program to find repeated consecutive letters
Mahnoor Ahmed
9 May 2014'''

def repeat(msg):
    #Messsage of length one can not have a set of 2 repeated characters hence forming the base case
    if len(msg)==1 or len(msg) == 0:
        return 0
    
    #checks whether the first 2 characters are the same and carries out recursive step on the remainder string if they are
    elif msg[0]==msg[1]:
        return 1 + repeat(msg[2:])
    
    #if first 2 characters are not the same, the recursive step just skips one character
    else:
        return repeat(msg[1:])

print("Number of pairs:",(repeat(msg=input("Enter a message:\n"))))