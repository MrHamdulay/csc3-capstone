print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
#Assigning values to yes/no
yes = 1
no = 0
qa = eval(input("Did anyone see you? (yes/no)\n"))#Letters are right hand side of flow chart questions(1st q)

if qa == 1:
    qb =eval(input("Was it a boss/lover/parent? (yes/no)\n"))
    
    if qb == 1:
        qc =eval(input("Was it expensive? (yes/no)\n"))
        
        if qc == 1:
            qd = eval(input("Can you cut off the part that touched the floor? (yes/no)\n"))
            
            if qd == 1:
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
            
        else:
            qe = eval(input("Is it chocolate? (yes/no)\n"))
            
            if qe == 1:
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
        
else:#Assuming no errors in the input otherwise USE elif q == 0
    q1 = eval(input("Was it sticky? (yes/no)\n"))#Numbers are left hand side of flow chart questions(1st q) **** Start coding here
    if q1 == 1:
       q2 =eval(input("Is it a raw steak? (yes/no)\n"))
        
       if q2 == 1:
            q4 = eval(input("Are you a puma? (yes/no)\n"))
            
            if q4  == 1:
               print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
       else:
            q5 = eval(input("Did the cat lick it? (yes/no)\n"))
            
        
            if q5 == 1:
                q6 = eval(input("Is your cat healthy? (yes/no)\n"))
                if q6 == 1:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
                
                
            else:
                print("Decision: Eat it.")
            
        
    else:
        q3 =eval(input("Is it an Emausaurus? (yes/no)\n"))
        
        if q3 == 1:
            q7 = eval(input("Are you a Megalosaurus? (yes/no)\n"))
            
            if q7 == 1:
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            q8 =eval(input("Did the cat lick it? (yes/no)\n")) 
            
            if q8 == 1:
               q9 = eval(input("Is your cat healthy? (yes/no)\n")) 
               
               if q9 == 1:
                   print("Decision: Eat it.")
               else:
                    print("Decision: Your call.")
               
            else:
               print("Decision: Eat it.") 
            
            
        
        