"""Assignment 8 Question 3
Yaseen Sulliman
6 May 2014"""

sentence = input("Enter a message:\n") # receive user input for message to be encrypted

def encrypt(answer):
    """encrypt the input message obtained"""
# The base case
    if answer == "":
        return ""
# check if the answer is in lower case
    elif answer[0].islower():
# check if the letter is 'z' to convert to 'a'
        if answer[0] == 'z':
            return 'a' + encrypt(answer[1:])
        else:    
            new_answer = ord(answer[0]) + 1
            return chr(new_answer)+encrypt(answer[1:])

    else:
        return answer[0]+encrypt(answer[1:])
    
print("Encrypted message:\n"+encrypt(sentence))
        
        
        