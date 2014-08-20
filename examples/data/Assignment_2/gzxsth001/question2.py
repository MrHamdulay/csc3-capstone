print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)\n")
if x=="yes":
  y=input("Was it a boss/lover/parent? (yes/no)\n")
  if y=="yes":
    z=input("Was it expensive? (yes/no)\n")
    if z=="yes":
      k=input("Can you cut off the part that touched the floor? (yes/no)\n")
      if k=="no":
          print("Decision: Your call.")
      elif k=="yes":
            print("Decision: Eat it.")
    elif z=="no":
        s=input("Is it chocolate? (yes/no)\n")
        if s=="yes":
            print("Decision: Eat it.")
        elif s=="no":
              print("Decision: Don't eat it.")
  elif y=="no":
        print("Decision: Eat it.")
elif x=="no":
    l=input("Was it sticky? (yes/no)\n")
    if l=="yes":
      m=input("Is it a raw steak? (yes/no)\n")
      if m=="yes":
        o=input("Are you a puma? (yes/no)\n")
        if o=="no":
            print("Decision: Don't eat it.")
        elif o=="yes":
              print("Decision: Eat it.")
      elif m=="no":
          n=input("Did the cat lick it? (yes/no)\n")
          if n=="no":
              print("Decision: Eat it.")
          elif n=="yes":
              q=input("Is your cat healthy? (yes/no)\n")
              if q=="no":
                  print("Decision: Your call.")
              elif q=="yes":
                    print("Decision: Eat it.")
    elif l=="no":
        f=input("Is it an Emausaurus? (yes/no)\n")
        if f=="no":
          n=input("Did the cat lick it? (yes/no)\n")
          if n=="no":
              print("Decision: Eat it.")
          elif n=="yes":
              q=input("Is your cat healthy? (yes/no)\n")
              if q=="no":
                  print("Decision: Your call.")
              elif q=="yes":
                    print("Decision: Eat it.")
        elif f=="yes":
            g=input("Are you a Megalosaurus? (yes/no)\n")
            if g=="no":
                print("Decision: Don't eat it.")          
            if g=="yes":        
                print("Decision: Eat it.")