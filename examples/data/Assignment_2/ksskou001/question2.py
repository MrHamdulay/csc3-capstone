print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
case1=input("Did anyone see you? (yes/no)\n")

if case1=="yes":
 
 a=input("Was it a boss/lover/parent? (yes/no)\n")
 if a=="yes":
  a1=input("Was it expensive? (yes/no)\n")
  if a1=="yes":
   a2=input("Can you cut off the part that touched the floor? (yes/no)\n")
   if a2=="yes":
    print("Decision: Eat it.")
   elif a2=="no":
    print("Decision: Your call.")
  elif a1=="no":
   a3=input("Is it chocolate? (yes/no)\n")
   if a3=="yes":
    print("Decision: Eat it.")
   elif a3=="no":
    print("Decision: Don't eat it.")
 elif a=="no":
  print("Decision: Eat it.")

elif case1=="no":
 b=input("Was it sticky? (yes/no)\n")
 if b=="yes":
  b1=input("Is it a raw steak? (yes/no)\n")
  if b1=="yes":
   b2=input("Are you a puma? (yes/no)\n")
   if b2=="yes":
    print("Decision: Eat it.")
   elif b2=="no":
    print("Decision: Don't eat it.")
  elif b1=="no":
   b3=input("Did the cat lick it? (yes/no)\n")
   if b3=="yes":
    b4=input("Is your cat healthy? (yes/no)\n")
    if b4=="no":
     print("Decision: Your call.")
    elif b4=="yes":
     print("Decision: Eat it.")
   else:
    print("Decision: Eat it.")
 elif b=="no":
  c=input("Is it an Emausaurus? (yes/no)\n")
  if c=="no":
   b3=input("Did the cat lick it? (yes/no)\n")
   if b3=="yes":
     b4=input("Is your cat healthy? (yes/no)\n")
     if b4=="no":
       print("Decision: Your call.")
     elif b4=="yes":
       print("Decision: Eat it.")
   else:
    print("Decision: Eat it.")
  elif c=="yes":
   d=input("Are you a Megalosaurus? (yes/no)\n")
   if d=="yes":
     print("Decision: Eat it.")
   elif d=="no":
     print("Decision: Don't eat it.")