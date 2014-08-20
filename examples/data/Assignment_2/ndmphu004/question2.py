#Assignment 2
#Question 2
#Phumelele Ndimande



def fall():
     
        print("Welcome to the 30 Second Rule Expert")
        print("------------------------------------")
        print("Answer the following questions by selecting from among the options.")  
        
        y = input("Did anyone see you? (yes/no)\n")
        if y== 'yes':
                z=input("Was it a boss/lover/parent? (yes/no)\n")
                if z == 'no':
                        print("Decision: Eat it.")
                else:
                        a= input("Was it expensive? (yes/no)\n")
                        if a=='yes':
                                b= input("Can you cut off the part that touched the floor? (yes/no)\n")
                                if  b=='yes': 
                                        print("Decision: Eat it.")
                                else:
                                                print("Decision: Your call.")
                        else:
                                c=input("Is it chocolate? (yes/no)\n")
                                if c=='yes':
                                        print("Decision: Eat it.")
                                else:
                                        print("Decision: Don't eat it.")
                                                       
        else:
                x= input("Was it sticky? (yes/no)\n")
                if x == 'yes':                 
                        d= input("Is it a raw steak? (yes/no)\n")
                        if d== 'yes':
                                e= input("Are you a puma? (yes/no)\n")
                                if e=='no':
                                        print("Decision: Don't eat it.")
                                else:
                                        print("Decision: Eat it.")
                        else:
                                f = input("Did the cat lick it? (yes/no)\n")
                                if f=='no':
                                        print("Decision: Eat it.")
                                else:
                                        g= input("Is your cat healthy? (yes/no)\n")
                                        if g=='yes':
                                                print("Decision: Eat it.")
                                        else:
                                                print("Decision: Don't eat it.")
        
                else:
                        h=input("Is it an Emausaurus? (yes/no)\n")
                        if h=='yes':
                                i= input("Are you a Megalosaurus? (yes/no)\n")
                                if i=='yes':
                                        print("Decision: Eat it.")
                                else:
                                        print("Decision: Don't eat it.")
                                
                        else:
                                j=input("Did the cat lick it? (yes/no)\n")
                                if j=='yes':
                                        k=input("Is your cat healthy? (yes/no)\n")
                                        if k=='yes':
                                                print("Decision: Eat it.")
                                        else:
                                                print("Decision: Your call.")
                                else:
                                        print("Decision: Eat it.")
           
fall()