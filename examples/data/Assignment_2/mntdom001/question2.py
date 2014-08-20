# question2.py
# Author: Dominic Manthoko
# 09 March 2014

def q2():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
    question = input("Did anyone see you? (yes/no) \n")
    ans0 = "yes"
    ans1 = "no"
    
    dec0 = "Eat it."
    dec1 = "Don't eat it."
    dec2 = "Your call."
    
    if question == ans0:                                                          
        q0 = input("Was it a boss/lover/parent? (yes/no) \n")                                
        if q0== ans1:                                                             
            print("Decision:",dec0)                                                        
        elif q0 == ans0:                                                           
            q1 =  input("Was it expensive? (yes/no) \n")                                    
            if q1 == ans0:                                                        
                q2 = input("Can you cut off the part that touched the floor? (yes/no) \n")   
                if q2 == ans0:                                                     
                    print("Decision:",dec0)                                                 
                elif q2 == ans1:                                                    
                    print("Decision:",dec2)                                              
            elif q1 == ans1:                                                 
                q3 = input("Is it chocolate? (yes/no) \n")                         
                if q3 == ans0:                                             
                    print("Decision:",dec0)                                        
                elif q3 == ans1:                                            
                    print("Decision:", dec1)                                    
                                                                 
    else:
        s0 = input("Was it sticky? (yes/no) \n")
        if s0 == ans0:
            s1 = input("Is it a raw steak? (yes/no) \n")
            if s1 == ans0:
                s2 = input("Are you a puma? (yes/no) \n")
                if s2 == ans0:
                    print("Decision:", dec0)
                elif s2 == ans1:
                    print("Decision:", dec1)
            elif s1 == ans1:
                s3 = input("Did the cat lick it? (yes/no) \n")
                if s3 == ans1:
                    print("Decision:", dec0)
                elif s3 == ans0:
                    s4 = input("Is your cat healthy? (yes/no) \n")
                    if s4 == ans0:
                        print("Decision:", dec0)
                    elif s4 == ans1:
                        print("Decision:", dec2)
                        
        elif s0 == ans1:
            s5 = input("Is it an Emausaurus? (yes/no) \n")
            if s5 == ans0:
                s4 = input("Are you a Megalosaurus? (yes/no) \n")
                if s4 == ans0:
                    print("Decision:", dec0)
                elif s4 == ans1:
                    print("Decision:", dec1)
            elif s5 == ans1:
                s6 = input("Did the cat lick it? (yes/no) \n")
                if s6 == ans0:
                    s7 = input("Is your cat healthy? (yes/no) \n")
                    if s7 == ans0:
                        print("Decision:", dec0)
                    elif s7 == ans1:
                        print("Decision:", dec2)
                if s6 == ans1:
                    print("Decision:", dec0)

q2()

    