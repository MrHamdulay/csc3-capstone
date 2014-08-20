#Program using a recursice function to count the number of pairs of repeated characters in a string
#KNNSAD001
#Assignment 8

#insert a message-input the text
text = input('Enter a message:\n')

number = 1

def repeated_letters(string):
    global number
    if string == '':
        return number
    else:

        #to check if the length of string is more than 1 character and
        #to check if the first letter in the word is the same as the one after it-second letter
        if len(string) > 1 and string[0] == string[1]:
            number += 1          
            
#introduce the recursive function :          
            
            return repeated_letters(string[2:len(string)])
        
        else:
            return repeated_letters(string[1:len(string)])



#print statement will show/display the number of repeated_letters in the string

print ('Number of pairs:', (repeated_letters(text)-1))