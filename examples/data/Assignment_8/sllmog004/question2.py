"""Assignment 8 Question 2
Yaseen Sulliman
5 May 2014"""

message = input("Enter a message:\n") # obtain input message from user

def count(answer):
    pairs = 0
    if len(answer) < 2:
        return pairs 
    else:
        if answer[0] == answer[1]:
            pairs+=1
            return pairs + count(answer[2:])
        else:
            return pairs + count(answer[1:])

print("Number of pairs:",count(message))
