#final version of Q2...I hope.

def displayTitle():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
def main():
    displayTitle()
    ans = input("Did anyone see you? (yes/no)\n")
    if ans=="yes":
         ans1=input("Was it a boss/lover/parent? (yes/no)\n")
         if ans1=="yes":
             ans2=input("Was it expensive? (yes/no)\n")
             if ans2=="yes":
                 ans3=input("Can you cut off the part that touched the floor? (yes/no)\n")
                 if ans3=="yes":
                     print("Decision: Eat it.")
                 elif ans3=="no":
                     print("Decision: Your call.")
                    
             elif ans2=="no":
                 ans4=input("Is it chocolate? (yes/no)\n")
                 if ans4=="yes":
                     print("Decision: Eat it.")
                 elif ans4=="no":
                     print("Decision: Don't eat it.")
                     
                     
         elif ans1=="no":
             print("Decision: Eat it.")
    elif ans=="no":
        ansN1=input("Was it sticky? (yes/no)\n")
        if ansN1=="yes":
            ansNY1=input("Is it a raw steak? (yes/no)\n")
            if ansNY1=="yes":
                ansNY2=input("Are you a puma? (yes/no)\n")
                if ansNY2=="yes":
                    print("Decision: Eat it.")
                elif ansNY2=="no":
                    print("Decision: Don't eat it.")
            elif ansNY1=="no":
                ansN3=input("Did the cat lick it? (yes/no)\n")
                if ansN3=="no":
                    print("Decision: Eat it.")
                elif ansN3=="yes":
                    ansN4=input("Is your cat healthy? (yes/no)\n")
                    if ansN4=="yes":
                        print("Decision: Eat it.")
                    elif ansN4=="no":
                        print("Decision: Your call.")
                    
                
            
        elif ansN1=="no":
            ansN2=input("Is it an Emausaurus? (yes/no)\n")
            if ansN2=="no":
                ansNN1=input("Did the cat lick it? (yes/no)\n")
                if ansNN1=="no":
                    print("Decision: Eat it.")
                if ansNN1=="yes":
                    ansNN2=input("Is your cat healthy? (yes/no)\n")
                    if ansNN2=="yes":
                        print("Decision: Eat it.")
                    elif ansNN2=="no": 
                        print("Decision: Your call.")
            elif ansN2=="yes":
                ansN3=input("Are you a Megalosaurus? (yes/no)\n")
                if ansN3=="yes":
                    print("Decision: Eat it.")
                if ansN3=="no":
                    print("Decision: Don't eat it.")
                
                    
            
            
    
            
         
        
        
                                                     
                                                     
                                                     
                                                     
main()                                                     
   