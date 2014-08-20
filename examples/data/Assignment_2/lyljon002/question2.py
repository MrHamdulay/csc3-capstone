#8 March 2014
#Assignment 2, Question 2
#Jonathan Leyland, LYLJON002

DecisionMade = bool
DecisionMade = False

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")



answer = input("Did anyone see you? (yes/no)\n")

if answer == "yes":
   answer = input("Was it a boss/lover/parent? (yes/no)\n") 
   if answer == "no" and DecisionMade == False:
      print("Decision: Eat it.")
      DecisionMade = True   
   if answer == "yes" and DecisionMade == False:
      answer = input("Was it expensive? (yes/no)\n")
      if answer == "yes" and DecisionMade == False:
         answer = input("Can you cut off the part that touched the floor? (yes/no)\n")
         if answer == "yes" and DecisionMade == False:
            print("Decision: Eat it.")
            DecisionMade = True
         if answer == "no" and DecisionMade == False:
            print("Decision: Your call.")
            DecisionMade = True
      if answer == "no" and DecisionMade == False:
         answer = input("Is it chocolate? (yes/no)\n")
         if answer == "yes" and DecisionMade == False:
            print("Decision: Eat it.")
            DecisionMade = True
         if answer == "no" and DecisionMade == False:
            print("Decision: Don't eat it.")
            DecisionMade = True
if answer == "no" and DecisionMade == False:
   answer = input("Was it sticky? (yes/no)\n")
   if answer == "yes" and DecisionMade == False:
      answer = input("Is it a raw steak? (yes/no)\n")
      if answer == "yes" and DecisionMade == False:
         answer = input("Are you a puma? (yes/no)\n")
         if answer == "yes" and DecisionMade == False:
            print("Decision: Eat it.")
            DecisionMade = True
         if answer == "no" and DecisionMade == False:
            print("Decision: Don't eat it.")
            DecisionMade = True
      if answer == "no" and DecisionMade == False:
         answer = input("Did the cat lick it? (yes/no)\n")
         if answer == "yes" and DecisionMade == False:
            answer = input("Is your cat healthy? (yes/no)\n")
            if answer == "yes" and DecisionMade == False:
               print("Decision: Eat it.")
               DecisionMade = True
            if answer == "no" and DecisionMade == False:
               print("Decison: Your call.")
               DecisionMade = True
         if answer == "no" and DecisionMade == False:
            print("Decision: Eat it.")
            DecisionMade = True
   if answer == "no" and DecisionMade == False:
      answer = input("Is it an Emausaurus? (yes/no)\n")
      if answer == "yes" and DecisionMade == False:
         answer = input("Are you a Megalosaurus? (yes/no)\n")
         if answer == "yes" and DecisionMade == False:
            print("Decision: Eat it.")
            DecisionMade = True
         if answer == "no" and DecisionMade == False:
            print("Decision: Don't eat it.")
            DecisionMade = True
      if answer == "no" and DecisionMade == False:
         answer = input("Did the cat lick it? (yes/no)\n")
         if answer == "yes" and DecisionMade == False:
            answer = input("Is your cat healthy? (yes/no)\n")
            if answer == "yes" and DecisionMade == False:
                  print("Decision: Eat it.")
                  DecisionMade = True
            if answer == "no" and DecisionMade == False:
                  print("Decision: Your call.")
                  DecisionMade = True
         if answer == "no" and DecisionMade == False:
            print("Decision: Eat it.")   
            DecisionMade = True