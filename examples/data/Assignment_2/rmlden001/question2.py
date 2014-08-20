# Question 2

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=(input("Did anyone see you? (yes/no)\n"))
if see=="yes":
   who=(input("Was it a boss/lover/parent? (yes/no)\n"))
   if who=="no":
      print("Decision: Eat it.")
   if who=="yes":
      cost=(input("Was it expensive? (yes/no)\n"))
      if cost=="yes":
         dirty=(input("Can you cut off the part that touched the floor? (yes/no)\n"))
         if dirty=="yes":
            print("Decision: Eat it.")
         if dirty=="no":
            print("Decision: Your call.")
      if cost=="no":
         chocolate=(input("Is it chocolate? (yes/no)\n"))
         if chocolate=="yes":
            print("Decision: Eat it.")
         if chocolate=="no":
            print("Decision: Don't eat it.")
if see=="no":
   sticky=(input("Was it sticky? (yes/no)\n"))
   if sticky=="no":
      Emausaurus=(input("Is it an Emausaurus? (yes/no)\n"))
      if Emausaurus=="no":
         cat=(input("Did the cat lick it? (yes/no)\n"))
         if cat=="no":
            print("Decision: Eat it.")
         if cat=="yes":
            healthy=(input("Is your cat healthy? (yes/no)\n"))
            if healthy=="yes":
               print("Decision: Eat it.")
            if healthy=="no":
               print("Decision: Your call.")
      if Emausaurus=="yes":
         Megalosaurus=(input("Are you a Megalosaurus? (yes/no)\n"))
         if Megalosaurus=="no":
            print("Decision: Don't eat it.")
         if Megalosaurus=="yes":
            print("Decision: Eat it.")
   if sticky=="yes":
      steak=(input("Is it a raw steak? (yes/no)\n"))
      if steak=="no":
         cat=(input("Did the cat lick it? (yes/no)\n"))
         if cat=="no":
            print("Decision: Eat it.")
         if cat=="yes":
            healthy=(input("Is your cat healthy? (yes/no)\n"))
            if healthy=="yes":
               print("Decision: Eat it.")
            if healthy=="no":
               print("Decision: Your call.")            
      if steak=="yes":
         puma=(input("Are you a puma? (yes/no)\n"))
         if puma=="yes":
            print("Decision: Eat it.")
         if puma=="no":
            print("Decision: Don't eat it.")
            