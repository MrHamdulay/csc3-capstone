print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")


        
print("Answer the following questions by selecting from among the options.")
     
anyonesee=input('Did anyone see you? (yes/no)' '\n')
if anyonesee=="no":
  sticky=input('Was it sticky? (yes/no)' "\n") 
  if sticky=="yes":
    rawsteak=input('Is it a raw steak? (yes/no)' "\n")
    if rawsteak=="yes":
      puma=input('Are you a puma? (yes/no)' "\n")
      if puma=="yes":
        print("Decision: Eat it.")
      if puma=="no":
        print("Decision: Don't eat it.")
    if rawsteak=='no':
      cat=input('Did the cat lick it? (yes/no)'"\n")
      if cat=='yes':
        healthy=input('Is your cat healthy? (yes/no)'"\n")
        if healthy=="yes":
          print("Decision: Eat it.")
        if healthy=="no":
          print('Decision: Your call.')
      if cat=="no":
        print('Decision: Eat it.')
  if sticky=="no":
    emausaurus=input('Is it an Emausaurus? (yes/no)'"\n")
    if emausaurus=="yes":
      megalosaurus=input('Are you a Megalosaurus? (yes/no)''\n') 
      if megalosaurus=="yes":
          print('Decision: Eat it.')
      if megalosaurus=='no':
        print("Decision: Don't eat it.")
    if emausaurus=='no':
      catlick=input('Did the cat lick it? (yes/no)' "\n")
      if catlick=='yes':
        heealthycat=input('Is your cat healthy? (yes/no)'"\n")
        if heealthycat=="yes":
          print('Decision: Eat it.')
        if heealthycat=="no":
          print('Decision: Your call.')
      if catlick=="no":
        print('Decision: Eat it.')
if anyonesee=="yes":
  lover=input('Was it a boss/lover/parent? (yes/no)'"\n")
  if lover=="no":
    print('Decision: Eat it.')
  if lover=='yes':
    expensive=input('Was it expensive? (yes/no)'"\n")
    if expensive=='no':
      chocolate=input('Is it chocolate? (yes/no)'"\n")
      if chocolate=="yes":
        print('Decision: Eat it.')
      if chocolate=="no":
        print("Decision: Don't eat it.")
    if expensive=="yes":
      cutoff=input('Can you cut off the part that touched the floor? (yes/no)'"\n")
      if cutoff=="yes":
        print('Decision: Eat it.')
      if cutoff=="no":
        print('Decision: Your call.') 