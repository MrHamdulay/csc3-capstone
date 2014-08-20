#question1
#Name: Shaheen Krodia
#Student Number: KRDSHA003
#Date:2014-03-12

#programme to determine if its okay to eat something 30 seconds after it has fallen on the floor

def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.") 
    
    A1=input("Did anyone see you? (yes/no)\n")
    
    if A1=="yes":
        A2=input("Was it a boss/lover/parent? (yes/no)\n")
        if A2=="yes":
            A3=input("Was it expensive? (yes/no)\n")
            if A3=="yes":
                A4=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if A4=="yes":
                    print("Decision: Eat it.")
                if A4=="no":
                    print("Decision: Your call.")
            
        
            
            if A3=="no":
                A4=input("Is it chocolate? (yes/no)\n")
                if A4=="yes":
                    print("Decision: Eat it.")
                if A4=="no":
                    print("Decision: Don't eat it.")
        if A2=="no": 
            print("Decision: Eat it.")            
                    
    if A1=="no":
        A2=input("Was it sticky? (yes/no)\n")
        if A2=="yes":
            A3=input("Is it a raw steak? (yes/no)\n")
            if A3=="yes":
                A4=input("Are you a puma? (yes/no)\n")
                if A4=="yes":
                    print("Decision: Eat it.")
                if A4=="no":
                    print("Decision: Don't eat it.")
            if A3=="no":
                A4=input("Did the cat lick it? (yes/no)\n")
                if A4=="yes":
                    A5=input("Is your cat healthy? (yes/no)\n")
                    if A5=="yes":
                        print("Decision: Eat it.")
                    if A5=="no":
                        print("Decision: Your call.")
                        
                if A4=="no":
                    print("Decision: Don't Eat it")
                          
        
        if A2=="no":
            A3=input("Is it an Emausaurus? (yes/no)\n")
            if A3=="yes":
                A4=input("Are you a Megalosaurus? (yes/no)\n")
                if A4=="yes":
                    print("Decision: Eat it.")
                    
                if A4=="no":
                    print("Decision: Don't eat it.")
                    
                
            if A3=="no":
                A4=input("Did the cat lick it? (yes/no)\n")
                if A4=="yes":
                    A5=input("Is your cat healthy? (yes/no)\n")
                    if A5=="yes":
                        print("Decision: Eat it.")
                        
                    if A5=="no":
                        print("Decision: Your call.")
                    
                if A4=="no":
                    print("Decision: Eat it.")
main()

                