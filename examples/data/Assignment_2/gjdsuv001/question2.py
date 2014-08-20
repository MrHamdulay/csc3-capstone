
#Program to follow a decision tree
#Written by: Suvir Gajadhur
#3 March 2014


print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

a = input("Did anyone see you? (yes/no)\n")

if a == 'yes' or a == 'Yes':
    b = input("Was it a boss/lover/parent? (yes/no)\n")
    if b == 'no':
        print("Decision: Eat it.")
    else:
        c = input("Was it expensive? (yes/no)\n")
        if c == 'yes' or c == 'Yes':
            d = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if d == 'yes' or d == 'Yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            e = input("Is it chocolate? (yes/no)\n")
            if e == 'yes' or e == 'Yes':
                            print("Decision: Eat it.")            
                            
            
            else:
             print("Decision: Don't eat it.")                
    
else:
    f = input("Was it sticky? (yes/no)\n")
    if f == 'yes' or f == 'Yes':
        g = input("Is it a raw steak? (yes/no)\n")
        if g == 'yes' or g == 'Yes':
            h = input("Are you a puma? (yes/no)\n")
            if h == "yes" or h == "Yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            i = input("Did the cat lick it? (yes/no)\n")
            if i =='yes' or i == 'Yes':
                j = input("Is your cat healthy? (yes/no)\n")
                if j == 'yes' or j == 'Yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        k = input("Is it an Emausaurus? (yes/no)\n")
        if k == 'yes' or k == 'Yes':
            l= input("Are you a Megalosaurus? (yes/no)\n")
            if l == 'yes' or l == 'Yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            m = input("Did the cat lick it? (yes/no)\n")
            if m =='yes' or m == 'Yes':
                n = input("Is your cat healthy? (yes/no)\n")
                if n == 'yes' or n == 'Yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            
    
    

    
         
         
