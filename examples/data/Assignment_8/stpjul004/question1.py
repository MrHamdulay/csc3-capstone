""" Word palindrome checker
 Author: Julius Stopf0rth (STPJUL004)
 Date: 2014-05-05 """

#Request user input and keep it on the DL
palin = input("Enter a string:\n").lower()

def check_palin(phrase):
    #Check f0r spaces
    #if phrase[0] == ' ':
    #    phrase = phrase[1:]
    #if phrase[len(phrase)-1] == ' ':
    #    phrase = phrase[:len(phrase)-1]
    #(A) Terminating step. Both even and odd palidromes (i.e 'kayak' or 'anna')
    if (len(phrase) <= 2) and (phrase[0] == phrase[len(phrase)-1]): 
        #If it has made it this far it must be a palindrome!
        print("Palindrome!")
    
    # If the string is longer than 2:
    # Check if the outermost characters are the same. 
    elif phrase[0] == phrase[len(phrase)-1]:
        #Recursive step. Remove the outermost characters and pass it on.
        check_palin(phrase[1:len(phrase)-1])
    
    #(B) Terminating step. If all else fails it is not a palindrome
    else:
        print("Not a palindrome!")

# Call the function
check_palin(palin)