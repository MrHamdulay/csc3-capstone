print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer=input("Did anyone see you? (yes/no)\n")
#if answer to first question is yes
if answer=='yes':
   who=input("Was it a boss/lover/parent? (yes/no)\n")
   if who=='yes':
      cost=input("Was it expensive? (yes/no)\n")
      if cost=='yes':
         cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
         if cut=='yes':
            print("Decision: Eat it.")
         elif cut=='no':
            print("Decision: Your call.")
      elif cost=='no':
         choc=input("Is it chocolate? (yes/no)\n")
         if choc=='yes':
            print("Decision: Eat it.")
         elif choc=='no':
            print("Decision: Don't eat it.")
   elif who=='no':
      print("Decision: Eat it.")
#if the answer to the first question is no
elif answer=='no':
   sticky=input("Was it sticky? (yes/no)\n")
   if sticky=='yes':
      steak=input("Is it a raw steak? (yes/no)\n")
      if steak=='yes':
         puma=input("Are you a puma? (yes/no)\n")
         if puma=='yes':
            print("Decision: Eat it.")
         elif puma=='no':
            print("Decision: Don't eat it.")
      elif steak=='no':
         cat=input("Did the cat lick it? (yes/no)\n")
         if cat=='yes':
            healthy=input("Is your cat healthy? (yes/no)\n")
            if healthy=='yes':
               print("Decision: Eat it.")
            elif healthy=='no':
               print("Decision: Your call.")
         elif cat=='no':
            print("Decision: Eat it.")
   elif sticky=='no':
      emau=input("Is it an Emausaurus? (yes/no)\n")
      if emau=='no':
         cat=input("Did the cat lick it? (yes/no)\n")
         if cat=='yes':
            healthy=input("Is your cat healthy? (yes/no)\n")
            if healthy=='yes':
               print("Decision: Eat it.")
            elif healthy=='no':
               print("Decision: Your call.")
         elif cat=='no':
            print("Decision: Eat it.")         
      elif emau=='yes':
         megalo=input("Are you a Megalosaurus? (yes/no)\n")
         if megalo=='yes':
            print("Decision: Eat it.")
         elif megalo=='no':
            print("Decision: Don't eat it.")