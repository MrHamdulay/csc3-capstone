#Taahirah achmat

def palindrone(p):
    if len(p)%2!=0:
        if len(p) == 1:
            return True
        elif p[0] == p[len(p)-1]: 
            return palindrone(p[1:len(p)-1])
        else:
            return False
    else:
        if len(p) == 0:
            return True
        elif p[0] == p[len(p)-1]: 
            return palindrone(p[1:len(p)-1])
        else:
            return False        
    

p = input("Enter a string:\n")
#p=p.replace(" ","")
x=palindrone(p)

if x:
    print("Palindrome!")
else:
    print("Not a palindrome!")