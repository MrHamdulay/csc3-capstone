def decisiontree():
     print("Welcome to the 30 Second Rule Expert")
     print("------------------------------------")
     print("Answer the following questions by selecting from among the options.")
     #-------------------------------------------------
     # Level 2
     def q2no():
         q2=input("Was it sticky? (yes/no)\n")
         if (q2=='no'):
             q3StickyNo()
         else:
             q3StickyYes()
     def q2yes():
         q2=input("Was it a boss/lover/parent? (yes/no)\n")
         if (q2=='no'):
                 eatIt()
         else:
             q3BossYes()
     #-------------------------------------------------
     # Level 3
     def q3BossYes():
         q3=input("Was it expensive? (yes/no)\n")
         if (q3=='no'):
             q4ExpensiveNo()
         else:
             q4ExpensiveYes()    
     #
     def q3StickyYes():
         q3=input("Is it a raw steak? (yes/no)\n")
         if (q3=='no'):
             q4EmasaurusNo()
         else:
             q3=input("Are you a puma? (yes/no)\n")
             if(q3=='yes'):
                 eatIt()
             else:
                 dontEatIt()
             
     def q3StickyNo():
         q3=input("Is it an Emausaurus? (yes/no)\n")
         if (q3=='no'):
             q4EmasaurusNo()
         else:
             q4EmasaurusYes()    
         
     #-------------------------------------------------
     #Level 4
     def q4EmasaurusYes():
         q4=input("Are you a Megalosaurus? (yes/no)\n")
         if (q4=='no'):
             dontEatIt()
         else:
            eatIt()
            
     def q4EmasaurusNo():
         q4=input("Did the cat lick it? (yes/no)\n")
         if (q4=='no'):
             eatIt()
         else:
            q5catLick()
     
     def q4ExpensiveYes():
         q4=input("Can you cut off the part that touched the floor? (yes/no)\n")
         if (q4=='no'):
             yourCall()
         else:
            eatIt()
     #       
     def q4ExpensiveNo():
         q4=input("Is it chocolate? (yes/no)\n")
         if (q4=='no'):
             dontEatIt()
         else:
             eatIt()  
             
     #-------------------------------------------------
     def q5catLick():
         q5=input("Is your cat healthy? (yes/no)\n")
         if (q5=='no'):
             yourCall()
         else:
            eatIt()
     #-------------------------------------------------
     
     
     
     
     
     def eatIt():
         print("Decision: Eat it.")
     def dontEatIt():
         print("Decision: Don't eat it.")
     def yourCall():
         print("Decision: Your call.")
         
     q1=input("Did anyone see you? (yes/no)\n")
     if(q1=='yes'):
         q2yes()
     else:
         q2no()     

decisiontree()     