q1=("Did anyone see you? (yes/no)"'\n')
q2=("Was it a boss/lover/parent? (yes/no)"'\n')
q3=("Was it expensive? (yes/no)"'\n')
q4=("Is it chocolate? (yes/no)"'\n')
q5=("Was it sticky? (yes/no)"'\n')
q6=("Is it a raw steak? (yes/no)"'\n')
q7=("Are you a puma? (yes/no)"'\n')
q8=("Can you cut off the part that touched the floor? (yes/no)"'\n')
q9=("Is it an Emausaurus? (yes/no)"'\n')
q10=("Did the cat lick it? (yes/no)"'\n')
q11=("Is your cat healthy? (yes/no)"'\n')
q12=("Are you a Megalosaurus? (yes/no)"'\n')

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

ans1=input(q1)
if ans1=="yes":
    ans2=input(q2)
    if ans2=="yes":
        ans3=input(q3)
        if ans3=="yes":
            ans8=input(q8)
            if ans8=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            ans4=input(q4)
            if ans4=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    ans5=input(q5)
    if ans5=="yes":
        ans6=input(q6)
        if ans6=="yes":
            ans7=input(q7)
            if ans7=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans10=input(q10)
            if ans10=="yes":
                ans11=input(q11)
                if ans11=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        ans9=input(q9)
        if ans9=="yes":
            ans12=input(q12)
            if ans12=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans10=input(q10)
            if ans10=="yes":
                ans11=input(q11)
                if ans11=="yes":
                    print("Decision: Eat it.") 
                    
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
            
            
            
            
            
            
            
            
        
        
                
   