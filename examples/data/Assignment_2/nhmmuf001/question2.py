# question2.py
# Mufudzi Nhamoinesu
# Program to determine whether to eat the food or not.

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

see = input("Did anyone see you? (yes/no)\n")
if see == "yes":
   who = input("Was it a boss/lover/parent? (yes/no)\n")
   if who == "yes":
      price = input("Was it expensive? (yes/no)\n")
      if price == "yes":
         clean = input("Can you cut off the part that touched the floor? (yes/no)\n")
         if clean =="yes":
            print("Decision: Eat it.")
         else:
            print("Decision: Your call.")
            
      else:
         chocolate = input("Is it chocolate? (yes/no)\n")
         if chocolate == "yes":
            print("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")
   
   else:
      print("Decision: Eat it.")
else:
   sticky = input("Was it sticky? (yes/no)\n")
   if sticky == "yes":
      steak = input("Is it a raw steak? (yes/no)\n")
      if steak == "yes":
         puma = input("Are you a puma? (yes/no)\n")
         if puma == "yes":
            print("Decision: Eat it.")
         else:
            print ("Decision: Don't eat it.")
      else:
         lick = input("Did the cat lick it? (yes/no)\n")
         if lick == "yes":
            healthy =  input("Is your cat healthy? (yes/no)\n")
            if healthy == "yes":
               print("Decision: Eat it.")
            else:
               print("Decision: Your call.")
         else:
            print("Decision: Eat it.")      
   else:
      dino1 = input("Is it an Emausaurus? (yes/no)\n")
      if dino1 == "yes" :
         dino2 = input("Are you a Megalosaurus? (yes/no)\n")
         if dino2 == "yes":
            print("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")
            
      else:
         cat = input("Did the cat lick it? (yes/no)\n")
         if cat == "yes":
            healthy =  input("Is your cat healthy? (yes/no)\n")
            if healthy == "yes":
               print("Decision: Eat it.")
            else:
               print("Decision: Your call.")
         else:
            print("Decision: Eat it.")