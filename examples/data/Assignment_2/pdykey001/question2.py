print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
def cat():
     if input("Did the cat lick it? (yes/no)\n")=="yes":
          if input("Is your cat healthy? (yes/no)\n")=="yes":
               print("Decision: Eat it.")
          else:
               print("Decision: Your call.")
     else:
          print("Decision: Eat it.")     
               
if input("Did anyone see you? (yes/no)\n")=="yes":
     if input("Was it a boss/lover/parent? (yes/no)\n")=="yes":
          if input("Was it expensive? (yes/no)\n")=="yes":
               if input("Can you cut off the part that touched the floor? (yes/no)\n")=="yes":
                    print("Decision: Eat it.")
               else:
                    print("Decision: Your call.")
          elif input("Is it chocolate? (yes/no)\n")=="yes":
               print("Decision: Eat it.")
          else:
               print("Decision: Don't eat it.")
     else:
          print("Decision: Eat it.")
elif input("Was it sticky? (yes/no)\n")=="yes":
     if input("Is it a raw steak? (yes/no)\n")=="yes":
          if input("Are you a puma? (yes/no)\n")=="yes":
               print("Decision: Eat it.")
          else:
               print("Decision: Don't eat it.")
     else: 
          cat()
     
elif input("Is it an Emausaurus? (yes/no)\n")=="yes":
     if input("Are you a Megalosaurus? (yes/no)\n")=="yes":
          print("Decision: Eat it.")
     else:
          print("Decision: Don't eat it.")
else: 
     cat()

