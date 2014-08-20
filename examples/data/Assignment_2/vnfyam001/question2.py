print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")

x=input("Did anyone see you? (yes/no)")
if(x=="yes"):
 y=input("\nWas it a boss/lover/parent? (yes/no)")
 if(y=="yes"):
   z=input("\nWas it expensive? (yes/no)")
   if(z=="yes"):
    v=input("\nCan you cut off the part that touched the floor? (yes/no)")
    if(v=="yes"):
      print("\nDecision: Eat it.")
    if(v=="no"):
      print("\nDecision: Your call.")
   if(z=="no"):
    p=input("\nIs it chocolate? (yes/no)")
    if(p=="yes"):
      print("\nDecision: Eat it.")
    if(p=="no"):
     print("\nDecision: Don't eat it.")          
 if(y=="no"): 
   print("\nDecision: Eat it.")

if(x=="no"):
  e=input("\nWas it sticky? (yes/no)")
  if(e=="yes"):
    r=input("\nIs it a raw steak? (yes/no)")
    if(r=="yes"):
     a=input("\nAre you a puma? (yes/no)")
     if(a=="yes"):
      print("\nDecision: Eat it.")
     if(a=="no"):
      print("\nDecision: Don't eat it.")
    if(r=="no"):
       avi=input("\nDid the cat lick it? (yes/no)")
       if(avi=="yes"):
        aviwe=input("\nIs your cat healthy? (yes/no)")
        if(aviwe=="yes"):
         print("\nDecision: Eat it.")
        if(aviwe=="no"):
         print("\nDecision: Your call.")
       if(avi=="no"):
        print("\nDecision: Eat it.")
  if(e=="no"):    
     ba=input("\nIs it an Emausaurus? (yes/no)")
     if(ba=="yes"):
      av=input("\nAre you a Megalosaurus? (yes/no)")
      if(av=="yes"):
       print("\nDecision: Eat it.")
      if(av=="no"):
       print("\nDecision: Don't eat it.")
     if(ba=="no"): 
      avi=input("\nDid the cat lick it? (yes/no)")
      if(avi=="yes"):
        aviwe=input("\nIs your cat healthy? (yes/no)")
        if(aviwe=="yes"):
         print("\nDecision: Eat it.")
        if(aviwe=="no"):
         print("\nDecision: Your call.")
      if(avi=="no"):
        print("\nDecision: Eat it.")
        
    