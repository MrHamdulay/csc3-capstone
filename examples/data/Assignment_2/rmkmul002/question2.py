print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
z=input("Did anyone see you? (yes/no)\n")
if z=="no":
 a=input("Was it sticky? (yes/no)\n")
 if a=="no":
     b=input("Is it an Emausaurus? (yes/no)\n")
     if b=="yes":
         c=input("Are you a Megalosaurus? (yes/no)\n")
         if c=="yes":
             print("Decision: Eat it.")
         elif c=="no":
               print("Decision: Don't eat it.")
     elif b=="no":
            d=input("Did the cat lick it? (yes/no)\n")
            if d=="yes":
                 e=input("Is your cat healthy? (yes/no)\n")
                 if e=="yes":
                      print("Decision: Eat it.")
                 elif e=="no":
                      print("Decision: Your call.")
            elif d=="no":
                  print("Decision: Eat it.")
    
 elif a=="yes":
  f=input("Is it a raw steak? (yes/no)\n")
  if f=="no":
   g=input("Did the cat lick it? (yes/no)\n")
   if g=="yes":
    i=input("Is your cat healthy? (yes/no)\n")
    if i=="yes":
     print("Decision: Eat it.")
    elif i=="no":
      print("Decision: Your call.")
   elif g=="no":
    print("Eat it.")
  elif f=="yes":
   j=input("Are you a puma? (yes/no)\n")
   if j=="yes":
    print("Decision: Eat it.")
   if j=="no":
    print("Decision: Don't eat it.")  
elif z=="yes":
 l=input("Was it a boss/lover/parent? (yes/no)\n")
 if l=="no":
  print("Decision: Eat it.")
 elif l=="yes":
  k=input("Was it expensive? (yes/no)\n")
  if k=="no":
   m=input("Is it chocolate? (yes/no)\n")
   if m=="no":
    print("Decision: Don't eat it. ")
   elif m=="yes":
    print("Decision: Eat it.")
  elif k=="yes":
   o=input("Can you cut off the part that touched the floor? (yes/no)\n")
   if o=="yes":
    print("Decision: Eat it.")
   elif o=="no":
    print("Decision: Your call.")
  