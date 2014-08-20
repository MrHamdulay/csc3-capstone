print ("Welcome to the 30 Second Rule Expert")
print ("-"*36) 
print ("Answer the following questions by selecting from among the options.")

decision = input("Did anyone see you? (yes/no)\n")
if decision == 'yes':
     decision1 = input("Was it a boss/lover/parent? (yes/no)\n")
     if decision1 == 'no':
          print ("Decision: Eat it.")     
     elif decision1 == 'yes':
          decision2 = input("Was it expensive? (yes/no)\n")
          if decision2 == 'yes':
               decision3 = input("Can you cut off the part that touched the floor? (yes/no)\n")
               if decision3 == 'yes':
                    print ("Decision: Eat it.")               
               else:
                    print ("Decision: Your call.")
          elif decision2 == 'no':
               decision4 = input("Is it chocolate? (yes/no)\n")
               if decision4 == 'no':
                    print ("Decision: Don't eat it.") 
               else:
                    print ("Decision: Eat it.") 

else:
     decisionA = input("Was it sticky? (yes/no)\n")
     if decisionA == 'yes':
          decisionB = input("Is it a raw steak? (yes/no)\n")
          if decisionB == 'yes':
               decisionC = input("Are you a puma? (yes/no)\n")
               if decisionC == 'yes':
                    print ("Decision: Eat it.")
               else:
                    print ("Decision: Don't eat it.")
          else:
               decisionD = input("Did the cat lick it? (yes/no)\n")
               if decisionD == 'no':
                    print ("Decision: Eat it.")
               else:    
                    decisionE = input("Is your cat healthy? (yes/no)\n")
                    if decisionE == 'no':
                         print ("Decision: Your call.")
                    else:
                         print ("Decision: Eat it.")
     
     else:
          decisionF = input("Is it an Emausaurus? (yes/no)\n")
          if decisionF == 'no':
               decisionG = input("Did the cat lick it? (yes/no)\n")
               if decisionG == 'no':
                    print ("Decision: Eat it.")
               else:    
                    decisionH = input("Is your cat healthy? (yes/no)\n")
                    if decisionH == 'no':
                         print ("Decision: Your call.")
                    else:
                         print ("Decision: Eat it.") 
          else:
               decisionI = input("Are you a Megalosaurus? (yes/no)\n")
               if decisionI == 'no':
                    print ("Decision: Don't eat it.")
               else:
                    print ("Decision: Eat it.")
                    
                    
                
               
                                                  
                               
                                                  
                                         