#deepak bhoojrajh 
#question 1

strings =input("Enter a string:\n")


def check(strings):
    
    if strings == '':
        return True
   
    else:
        if (ord(strings[0]) == ord(strings[len(strings)-1])):
            return check(strings[1:len(strings)-1])
        else:
            return False



if(check(strings)==True):
    print("Palindrome!")

else:
    print("Not a palindrome!")