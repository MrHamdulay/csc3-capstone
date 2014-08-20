print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

x =(input("Did anyone see you? (yes/no)\n"))

if x=="yes":
 y =(input("Was it a boss/lover/parent? (yes/no)\n"))
 if y=="no":
  print("Decision: Eat it.")
 if y=="yes":
  z =(input("Was it expensive? (yes/no)\n"))
  if z=="no":
   b =(input("Is it chocolate? (yes/no)\n"))
   if b=="no":
    print("Decision: Don't eat it.")
   if b=="yes":
    print("Decision: Eat it.")
  if z=="yes":
    a =(input("Can you cut off the part that touched the floor? (yes/no)\n"))
    if a=="yes":
          print("Decision: Eat it.")    
    if a=="no":
      print("Decision: Your call.")
if x=="no":
 c =(input("Was it sticky? (yes/no)\n"))
 if c=="yes":
  d =(input("Is it a raw steak? (yes/no)\n"))
  if d=="yes":
     e =(input("Are you a puma? (yes/no)\n"))
     if e=="no":
      print("Decision: Don't eat it.")
     if e=="yes":
      print("Decision: Eat it.")  
  if d=="no":
   f =(input("Did the cat lick it? (yes/no)\n"))
   if f=="yes":
    g =(input("Is your cat healthy? (yes/no)\n"))
    if g=="yes":
     print("Decision: Eat it.")
    if g=="no":
     print("Decision: Your call.")
   if f=="no":
    print("Decision: Eat it.") 
 if c=="no":
  h =(input("Is it an Emausaurus? (yes/no)\n"))
  if h=="yes":
   k =(input("Are you a Megalosaurus? (yes/no)\n"))
   if k=="yes":
    print("Decision: Eat it.")
   if k=="no":
    print("Decision: Don't eat it.")
  if h=="no":
   i =(input("Did the cat lick it? (yes/no)\n"))
   if i=="yes":
    j =(input("Is your cat healthy? (yes/no)\n"))
    if j=="yes":
     print("Decision: Eat it.")
    if j=="no":
     print("Decision: Your call.")
   if i=="no":
    print("Decision: Eat it.")
   

    
