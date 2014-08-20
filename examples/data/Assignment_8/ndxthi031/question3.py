#Thiolan Prevan Naidoo
#NDXTHI031
#question1  
#encrypt a string

a=""
def operate(word): 
    global a
    if word=='':
        return a
    elif (ord(word[0])>96 and ord(word[0])<122):#checks if the character is a lower_case letter from a-y
        a=a+chr(ord(word[0])+1)#adds the letter after the character to a string a
        return operate(word[1:len(word)])#sends the string recieved without the first character back into the function operate
    elif (ord(word[0])==122):#checks if the character is a lower_case z
        a=a+'a'#adds the character a back to the string a
        return operate(word[1:len(word)])  
    else:
        a=a+word[0] #adds the character to the string a if its not a lowercase letter
        return operate(word[1:len(word)])  
        
x=input("Enter a message:\n")
print("Encrypted message:")
print(operate(x))
