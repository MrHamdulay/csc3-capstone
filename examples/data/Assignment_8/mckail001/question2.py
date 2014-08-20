"""Ailsa Mackay MCKAIL001
Assignment 8 Question 2 
2014-05-06"""

def adjacent_pairs(message):
    if len(message) == 1:
        return 0
    elif len(message) == 2:
        if message[0] == message[1]:
            return 1
        else:
            return 0
    elif message[0] == message[1]:
        return 1 + adjacent_pairs(message[2::]) #adds one to count if adjacent letters are equal
    else:
        return adjacent_pairs(message[1::]) #if adjacent letters are not equal, move onto next iteration

def main():
    message = input("Enter a message:\n")
    print("Number of pairs:",adjacent_pairs(message))

main()

