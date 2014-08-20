print("Welcome to the 30 Second Rule Expert")
print('------------------------------------')
print("Answer the following questions by selecting from among the options.")
y=input('Did anyone see you? (yes/no)\n')
if (y=="yes"):
   y=input('Was it a boss/lover/parent? (yes/no)\n')
   if (y=="yes"):
      y=input('Was it expensive? (yes/no)\n')
      if (y=="yes"):
         y=input('Can you cut off the part that touched the floor? (yes/no)\n')
         if (y=="yes"):
            print("Decision: Eat it.")
         elif (y=="no"):
            print('Decision: Your call.')
      elif (y=='no'):
         y==('Is it chocolate? (yes/no)\n')
         if (y=="yes"):
            print('Decision: Eat it.')
         elif (y=='no'):
            print("Decision: Don't eat it.")
   elif (y=='no'):
      print('Decision: Eat it.')
elif (y=='no'):
   y=input('Was it sticky? (yes/no)\n')
   if (y=='yes'):
      y=input('Is it a raw steak? (yes/no)\n')
      if (y=='yes'):
         y=input('Are you a puma? (yes/no)\n')
         if (y=='yes'):
            print('Decision: Eat it.')
         elif (y=='no'):
            print("Decision: Don't eat it.")
      elif (y=='no'):
         y=input('Did the cat lick it? (yes/no)\n')
         if (y=='yes'):
            y=input('Is your cat healthy? (yes/no)\n')
            if (y=="yes"):
               print("Decision: Eat it.")
            elif (y=="no"):
               print('Decision: Your call.')
         elif (y=='no'):
            print('Decision: Eat it.')
   elif (y=='no'):
      y=input('Is it an Emausaurus? (yes/no)\n')
      if (y=='yes'):
         y=input('Are you a Megalosaurus? (yes/no)\n')
         if (y=='yes'):
            print("Decision: Eat it.")
         elif (y=='no'):
            print("Decision: Don't eat it.")
      elif (y=='no'):
         y=input('Did the cat lick it? (yes/no)\n')
         if (y=='yes'):
            y=input('Is your cat healthy? (yes/no)\n')
            if (y=="yes"):
               print("Decision: Eat it.")
            elif (y=="no"):
               print('Decision: Your call.')
         elif (y=='no'):
            print('Decision: Eat it.')      