"""counting number of pairs
tinashe choga
5/4/ 2014"""

# function to count the number of pairs
def count_pairs (message):
    if len(message)==1:
        return 0
    elif len(message)==2:
        if message[0]==message[1]:
            return 1
        else:
            return 0
    elif message[0] == message[1]:
        return 1 + count_pairs(message[2:])
    else:
        return 0 + count_pairs(message[1:])
"""printing out the number"""
message=input("Enter a message:\n")
y=count_pairs(message)  #calling the function and assigning it to a variable
print("Number of pairs:",y)

