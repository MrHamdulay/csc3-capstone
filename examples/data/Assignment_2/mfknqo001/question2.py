print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

a=input("Did anyone see you? (yes/no)\n")
if (a=='yes'):
   b=input("Was it a boss/lover/parent? (yes/no)\n")
   if (b=='yes'):
      l=input("Was it expensive? (yes/no)\n")
      if (l=='yes'):
         c=input("Can you cut off the part that touched the floor? (yes/no)\n")
         if (c=='yes'):
            print("Decision: Eat it.\n")
         else:
            print("Decision: Your call.\n")
      else:
         d=input("Is it chocolate? (yes/no)\n")
         if (d=='yes'):
            print("Decision: Eat it.\n")
         else:
            print("Decision: Don't eat it.\n")
   else:
      print("Decision: Eat it.\n") 
else:
   e=input("Was it sticky? (yes/no)\n")
   if (e=='yes'):
      f=input("Is it a raw steak? (yes/no)\n")
      if (f=='yes'):
         g=input("Are you a puma? (yes/no)\n")
         if (g=='yes'):
            print("Decision: Eat it.\n")
      else:
         h=input("Did the cat lick it? (yes/no)\n")
         if (h=='yes'):
            i=input("Is your cat healthy? (yes/no)\n")
            if (i=='yes'):
               print("Decision: Eat it.\n")
            else:
               print("Decision: Your call.\n")
         else:
            print("Decision: Eat it.\n")
   else:
      j=input("Is it an Emausaurus? (yes/no)\n")
      if (j=='yes'):
         k=input("Are you a Megalosaurus? (yes/no)\n")
         if (k=='yes'):
            print("Decision: Eat it.\n")
         else:
            print("Decision: Don't eat it.\n")
      else:
         h=input("Did the cat lick it? (yes/no)\n")
         if (h=='yes'):
            i=input("Is your cat healthy? (yes/no)\n")
            if (i=='yes'):
               print("Decision: Eat it.\n")
            else:
               print("Decision: Your call.\n")   
         else:
            print("Decision: Eat it.\n")