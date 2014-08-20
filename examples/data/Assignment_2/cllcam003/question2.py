print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=input("Did anyone see you? (yes/no)\n")
if see== "yes": 
   who=input("Was it a boss/lover/parent? (yes/no)\n")   
   if who== "yes":
      price=input("Was it expensive? (yes/no)\n")
      if price== "yes":
         cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
         if cut== "yes":
            print("Decision: Eat it.")
         elif cut== "no":
            print("Decision: Your call.")
      elif price== "no":
         chocolate=input("Is it chocolate? (yes/no)\n")
         if chocolate== "yes":
            print("Decision: Eat it.")
         elif chocolate== "no":
               print("Decision: Don't eat it.")
   elif who== "no":
      print("Decision: Eat it.")
elif see== "no":
   sticky=input("Was it sticky? (yes/no)\n")
   if sticky== "yes":
      raw=input("Is it a raw steak? (yes/no)\n")
      if raw== "yes":
         puma=input("Are you a puma? (yes/no)\n")
         if puma== "yes":
            print("Decision: Eat it.")
         elif puma== "no":
            print("Decision: Don't eat it.")
      elif raw== "no":
         cat=input("Did the cat lick it? (yes/no)\n")
         if cat== "yes":
            healthy=input("Is your cat healthy? (yes/no)\n")
            if healthy== "yes":
               print("Decision: Eat it.")
            elif healthy== "no":
               print("Decision: Your call.")
         elif cat== "no":
            print("Decision: Eat it.")
   elif sticky== "no":
      ema= input("Is it an Emausaurus? (yes/no)\n")
      if ema== "yes":
         mega=input("Are you a Megalosaurus? (yes/no)\n")
         if mega== "yes":
            print("Decision: Eat it.")
         elif mega== "no":
            print("Decision: Don't eat it.")
      elif ema== "no":
         cat2=input("Did the cat lick it? (yes/no)\n")
         if cat2== "yes":
            healthy2=input("Is your cat healthy? (yes/no)\n")
            if healthy2== "yes":
               print("Decision: Eat it.")
            elif healthy2== "no":
               print("Decision: Your call.")
         elif cat2== "no":
            print("Decision: Eat it.")
      
         
            
          
      