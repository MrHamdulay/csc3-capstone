#you dropped food on the floor do you eat it.

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q1=input("Did anyone see you? (yes/no) \n") 
if q1== "yes":
    q12=input("Was it a boss/lover/parent? (yes/no)\n")
    if q12=="yes":
        q123=input("Was it expensive? (yes/no)\n")
        if q123=='yes':
            q1234=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q1234=='yes':
                print("Decision: Eat it.")
            else:
             print("Decision: Your call.")
        elif q123 =='no':
             q2=input("Is it chocolate? (yes/no)\n")
             if q2=='yes':
                print("Decision: Eat it.")
             else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
elif q1=="no":
    c=input("Was it sticky? (yes/no)\n")
    if c=='yes':
       d=input("Is it a raw steak? (yes/no)\n")
       if d=='yes':
         e=input("Are you a puma? (yes/no)\n")
         if e =='yes':
           print("Decision: Eat it.")
         else:
           print("Decision: Don't eat it.")
       elif d=='no':
         f=input("Did the cat lick it? (yes/no)\n")
         if f=='no':
            print("Decision: Eat it.")
         elif f=='yes':
          g=input("Is your cat healthy? (yes/no)\n")
          if g=='yes':
                print("Decision: Eat it.")
          else:
              print("Decision: Your call.")
    elif c=='no':
       h=input("Is it an Emausaurus? (yes/no)\n")
       if h=='yes':
           j=input("Are you a Megalosaurus? (yes/no)\n")
           if j=='yes':
               print("Decision: Eat it.")
           else:
               print("Decision: Don't eat it.")
       elif h=='no':
         k=input("Did the cat lick it? (yes/no)\n")
         if k=='no':
               print("Decision: Eat it.")
         elif k=='yes':
             l=input("Is your cat healthy? (yes/no)\n")
             if l=='yes':
                 print("Decision: Eat it.")
               
             else:
                print("Decision: Your call.")
       
        
        

       
        

            
        
 
    