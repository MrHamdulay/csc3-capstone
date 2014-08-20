# Mikhaila Sorour
# 12 March 2014
# Program to decide if you should eat your dropped food
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see = input("Did anyone see you? (yes/no)\n")
if see=="yes":
   parent = input ("Was it a boss/lover/parent? (yes/no)\n")
   if parent=="yes":
      expensive = input("Was it expensive? (yes/no)\n")
      if expensive==("yes"):
         cutoff=input("Can you cut off the part that touched the floor? (yes/no)\n")
         if cutoff==("yes"):
            print("Decision: Eat it.")
         else:
            print("Decision: Your call.")
      else:
         chocolate = input("Is it chocolate? (yes/no)\n")
         if chocolate==("yes"):
            print("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")
   else:
      print("Decision: Eat it.")
else:
   sticky=input("Was it sticky? (yes/no)\n")
   if sticky==("yes"):
      raw=input("Is it a raw steak? (yes/no)\n")
      if raw==("yes"):
         puma=input("Are you a puma? (yes/no)\n")
         if puma==("yes"):
            print("Decision: Eat it.")
         else: 
            print("Decision: Don't eat it.")
      else:
         lick1=input("Did the cat lick it? (yes/no)\n")
         if lick1==("yes"):
            healthy1=input("Is your cat healthy? (yes/no)\n")
            if healthy1==("yes"):
               print("Decision: Eat it.")
            else:
               print("Decision: Your call")
         else:
            print("Decision: Eat it.")
   else:
      ema=input("Is it an Emausaurus? (yes/no)\n")
      if ema==("yes"):
         mega=input("Are you a Megalosaurus? (yes/no)\n")
         if mega==("yes"):
            print("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")
      else:
         lick2=input("Did the cat lick it? (yes/no)\n")
         if lick2==("yes"):
            healthy2=input("Is your cat healthy? (yes/no)\n")
            if healthy2==("yes"):
               print("Decision: Eat it.")
            else:
               print("Decision: Your call.")
         else:
            print("Decision: Eat it.")
                     
