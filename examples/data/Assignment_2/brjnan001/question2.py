def DoYouEatIt():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    x=input("Did anyone see you? (yes/no)\n")
    if(x=='yes'):
        y=input("Was it a boss/lover/parent? (yes/no)\n")
        if (y=='yes'):
            z=input("Was it expensive? (yes/no) \n")
            if (z=='yes'):
                n=input("Can you cut off the part that touched the floor? (yes/no)\n") 
                if(n=='yes'):
                    print("Decision: Eat it.")
                else:
                    if (n=='no'):
                        print("Decision: Your call.")                
            else:
                if (z=='no'):
                    j=input("Is it chocolate? (yes/no) \n")
                    if(j=='yes'):
                        print("Decision: Eat it.")
                    else:
                        if (j=='no'):
                            print("Decision: Don't eat it.")                 
        else:
            if (y=='no'):
                print("Decision: Eat it.")
        
    else:
        if(x=='no'):
                q=input("Was it sticky? (yes/no)\n")  
                if(q=='yes'):
                    s=input("Is it a raw steak? (yes/no) \n")
                    if(s=='yes'):
                        f=input("Are you a puma? (yes/no) \n")
                        if(f=='yes'):
                            print("Decision: Eat it.")
                        else:
                            if (f=='no'):
                                print("Decision: Don't eat it.")                                    
                    else:
                        if (s=='no'):
                            t=input("Did the cat lick it? (yes/no) \n") 
                            if(t=='yes'):
                                w=input("Is your cat healthy? (yes/no) \n")
                                if(w=='yes'):
                                    print("Decision: Eat it.")
                                else:
                                    if(w=='no'):
                                        print("Decision: Your call.")                                 
                            else:
                                if (t=='no'):
                                    print("Decision: Eat it.")                                          
                else:
                    if (q=='no'):
                        r=input("Is it an Emausaurus? (yes/no) \n")
                        if(r=='yes'):
                            m=input("Are you a Megalosaurus? (yes/no) \n")
                            if(m=='yes'):
                                print("Decision: Eat it.")
                            else:
                                if (m=='no'):
                                    print("Decision: Don't eat it.")                              
                        else:
                            if (r=='no'):
                                a=input("Did the cat lick it? (yes/no) \n") 
                                if a=='no':
                                    print("Decision: Eat it.")
                                else:
                                    if a=='yes':
                                        cat=input("Is your cat healthy? (yes/no)\n")
                                        if cat=='yes':
                                            print("Decision: Eat it.")
                                        else:
                                            print("Decision: Your call.")  
                                                
                                            
                                  
                       
                                      
DoYouEatIt()
