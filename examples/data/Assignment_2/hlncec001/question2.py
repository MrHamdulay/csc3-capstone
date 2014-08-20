#HLNCEC00
#3/7/2014
#Assignment 2
#Question 2
def Rule_Expect():
   print()
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

a1 = input("Did anyone see you? (yes/no)\n")
if(a1=='yes'):
   a2 = input("Was it a boss/lover/parent? (yes/no)\n")
   if(a2=='no'):
      print("Decision: Eat it.")
   if(a2=='yes'):
      a3 = input("Was it expensive? (yes/no)\n")
      if(a3=='yes'):
         a4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
         if (a4=='yes'):
            print("Decision: Eat it.")
         else:
            print("Decision: Your call.")
      else:
         a5 = input("Is it chocolate? (yes/no)\n")
         if (a5=='yes'):
            print('Decision: Eat it.')
         else:
            print("Decision: Don't eat it.")
else:
   a6 = input("Was it sticky? (yes/no)\n")
   if (a6=='yes'):
      a7 = input("Is it a raw steak? (yes/no)\n")
      if (a7=='yes'):
         a8 = input("Are you a puma? (yes/no)\n")
         if (a8=='no'):
            print("Decision: Don't eat it.")
         else:
            print("Decision: Eat it.")
      else: 
         a9 = input("Did the cat lick it? (yes/no)\n")
         if (a9=='yes'):
            a10 = input("Is your cat healthy? (yes/no)\n")
            if (a10=='no'):
               print('Decision: Your call.')
            else:
               print('Decision: Eat it.')
         else:
            print('Decision: Eat it.')
   else:
      a11 = input("Is it an Emausaurus? (yes/no)\n")
      if (a11=='yes'):
         a12 = input("Are you a Megalosaurus? (yes/no)\n")
         if (a12=='yes'):
            print("Decision: Eat it.")
         else:
            print("Decision: Don't eat it.")
      else:
         a13 = input("Did the cat lick it? (yes/no)\n")
         if (a13=='yes'):
            a14 = input("Is your cat healthy? (yes/no)\n")
            if (a14=='no'):
               print('Decision: Your call.')
            else:
                  print("Decision: Eat it.")
         else:
            print('Decision: Eat it.')
Rule_Expect()