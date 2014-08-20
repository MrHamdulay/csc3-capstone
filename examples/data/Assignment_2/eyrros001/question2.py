print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

a = input("Did anyone see you? (yes/no)\n").lower()
eat = False
call = False


if a[0]=='y':
    a = input("Was it a boss/lover/parent? (yes/no)\n").lower()
    if a[0]=='y':
        a = input("Was it expensive? (yes/no)\n").lower()       
        if a[0]=='y':
            a = input("Can you cut off the part that touched the floor? (yes/no)\n").lower()   
            if a[0]=='y':
                eat = True
            else:
                call = True
        else:
            a = input("Is it chocolate? (yes/no)\n").lower()
            if a[0]=='y':
                eat = True
            else:
                eat = False  
    else:
        eat = True
else:
    a = input("Was it sticky? (yes/no)\n").lower()
    if a[0]=='y':
        a = input("Is it a raw steak? (yes/no)\n").lower()
        if a[0]=='y':
            a = input("Are you a puma? (yes/no)\n").lower()        
            if a[0]=='y':
                eat = True
            else:
                eat = False
        elif a[0]=='n':
            a = input("Did the cat lick it? (yes/no)\n").lower()
            if a[0]=='y':
                a = input("Is your cat healthy? (yes/no)\n").lower()
                if a[0]=='y':
                    eat = True
                else:
                    call = True
            else:
                eat = True                        
    else:
        a = input("Is it an Emausaurus? (yes/no)\n").lower()
        if a[0]=='y':
            a = input("Are you a Megalosaurus? (yes/no)\n").lower()
            if a[0]=='y':
                eat = True
            else:
                eat = False
        else:
            a = input("Did the cat lick it? (yes/no)\n").lower()
            if a[0]=='y':
                a = input("Is your cat healthy? (yes/no)\n").lower()
                if a[0]=='y':
                    eat = True
                else:
                    call = True
            else:
                eat = True            
                
                

#determine if must eat
if(call):
    print("Decision: Your call.")
elif eat:
    print("Decision: Eat it.")
else:
    print("Decision: Don't eat it.")
        
        