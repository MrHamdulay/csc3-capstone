def palindrone(phrase):
    if len(phrase)%2!=0:
        if len(phrase) == 1:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palindrone(phrase[1:len(phrase)-1])
        else:
            return False
    else:
        if len(phrase) == 0:
            return True
        elif phrase[0] == phrase[len(phrase)-1]: 
            return palindrone(phrase[1:len(phrase)-1])
        else:
            return False        
    

phrase = input("Enter a string:\n")
#phrase=phrase.replace(" ","")
y=palindrone(phrase)

if y:
    print("Palindrome!")
else:
    print("Not a palindrome!")