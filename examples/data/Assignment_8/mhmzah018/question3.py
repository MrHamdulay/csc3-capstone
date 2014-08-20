"""Assignment 8 - question 3
Zaheer Mahmood
04 - 05 - 2014"""

sentence = input("Enter a message:\n")

def encrypt(answer):
#base case
    if answer == "":
        return ""
#check if answer is lower case
    elif answer[0].islower():
#check if letter is z to convert to a
        if answer[0] == 'z':
            return 'a' + encrypt(answer[1:])
#continue to recurse through function
        else:    
            new_answer = ord(answer[0]) + 1
            return chr(new_answer)+encrypt(answer[1:])

    else:
        return answer[0]+encrypt(answer[1:])
    
print("Encrypted message:\n"+encrypt(sentence))
        
        
        