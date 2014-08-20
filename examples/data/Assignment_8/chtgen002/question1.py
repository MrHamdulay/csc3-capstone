"""CHTGEN002
09/05/2014
Palindrome!"""

sen_input = input ("Enter a string:\n") #input of sentence

def check (sen_input): 

    if sen_input == '':
        return True

    else:
        if ( (ord(sen_input[len(sen_input)-1])) == (ord(sen_input[0]))): 
            return check(sen_input[1:len(sen_input)-1]) #reverses string

        else:
            return False

if (check(sen_input) == True): #if returned value is true
    print ("Palindrome!")
    
else:
    print ("Not a palindrome!")