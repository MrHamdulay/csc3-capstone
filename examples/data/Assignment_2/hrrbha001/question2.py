#b harrilal
#5 march 2014
#30 sec rule flowchart

print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")


seen = input ("Did anyone see you? (yes/no)\n")
if seen == "yes":
   person = input ("Was it a boss/lover/parent? (yes/no)\n")
   if person == "yes":
      expensive = input ("Was it expensive? (yes/no)\n")
      if expensive == "yes":
         floor = input ("Can you eat the part that touched the floor? (yes/no)\n")
         if floor == "yes":
            print ("Decision: Eat it.")
         else:
            print ("Decision: Your call.")
      else:
         chocolate = input ("Is it chocolate? (yes/no)\n")
         if chocolate == "yes":  
            print ("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")   
   else:
      print("Decision: Eat it.")
      
else:
   sticky = input ("Was it sticky? (yes/no)\n")
   if sticky == "yes":      
      steak = input("Is it a raw steak? (yes/no)\n")
      if steak== "yes":
         puma = input("Are you a puma? (yes/no)\n")
         if puma=="yes":
               print("Decision: Eat it.")
         else:
               print("Decision: Don't eat it.") 
      else:
         cat = input("Did the cat lick it? (yes/no)\n")
         if cat=="yes":
            healthy =  input("Is the cat healthy? (yes/no)\n")
            if healthy =="yes":
               print("Decision: Eat it.")
            else:
               print("Decision: Your call.")
         else:
            print("Decision: Eat it.")
   else:
      emausaurus = input("Is it an Emausaurus? (yes/no)\n")
      if emausaurus =="yes":
         mega = input("Are you a Megalosaurus?(yes/no)\n")
         if mega == "yes":
            print("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")
      else:
         cat = input("Did the cat lick it? (yes/no)\n")
         if cat=="yes":
            healthy =  input("Is the cat healthy? (yes/no)\n")
            if healthy =="yes":
               print("Decision: Eat it.")
            else:
               print("Decision: Your call.")
         else:
            print("Decision: Eat it.")
      
   