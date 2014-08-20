print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
txt1=input("Did anyone see you? (yes/no)\n")
if txt1=='yes':
    txt2=input("Was it a boss/lover/parent? (yes/no)\n")
    if txt2=='no':
        print("Decision: Eat it.")
    else :
        if txt2=='yes':
            txt3=input("Was it expensive? (yes/no)\n")
            if txt3=='no':
                txt4=input("Is it chocolate? (yes/no)\n")
                if txt4=='yes':
                    print("Decision: Eat it.")     
                else :
                    if  txt4=='no':
                        print("Decision: Don't eat it.")
            else :
                if txt3=='yes':
                    txt17=input("Can you cut off the part that touched the floor? (yes/no)\n")
                    if txt17=='no':
                        print("Decision: Your call.")
                    else :
                        if txt17=='yes':
                            print("Decision: Eat it.")
else :
    if txt1=='no':
        txt10=input("Was it sticky? (yes/no)\n")
        if txt10=='no':
            txt11=input("Is it an Emausaurus? (yes/no)\n")
            if txt11=='yes':
                txt12=input("Are you a Megalosaurus? (yes/no)\n")
                if txt12=='no':
                        print("Decision: Don't eat it.")
                else :
                    if txt12=='yes':
                        print("Decision: Eat it." )
    
            else :
                if txt11=='no':
                    txt11=input("Did the cat lick it? (yes/no)\n")
                    if txt11=='no':
                        print("Decision: Eat it.")
                    else :
                        if txt11=='yes':
                            txt11=input("Is your cat healthy? (yes/no)\n")
                            if txt11=='no':
                                print("Decision: Your call.")
                            else :
                                if txt11=='yes':
                                    print("Decision: Eat it.")
        else:                
            if txt10=='yes':
                txt9=input("Is it a raw steak? (yes/no)\n")
                if txt9=='yes':
                    txt13=input("Are you a puma? (yes/no)\n")             
                    if txt13=='no':
                        print("Decision: Don't eat it.")
                    else :
                        if txt13=='yes':
                            print("Decision: Eat it.")
                else :
                    if txt9=='no':
                        txt14=input("Did the cat lick it? (yes/no)\n")
                        if txt14=='yes':
                            txt15=input("Is your cat healthy? (yes/no)\n")
                            if txt15=='no':
                                print("Decision: Your call.")
                            else :
                                if txt15=='yes':
                                    print("Decision: Eat it.")
                                
                        else :
                            if txt14=='no':
                                print("Decision: Eat it.")
                            else :
                                if txt15=='yes':
                                    print("Decision: Eat it,")
                                 
                             
                            
                            
                        
                        
                                                
                            
                                                                

                        
                            
        
    