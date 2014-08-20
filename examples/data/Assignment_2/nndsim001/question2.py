# This program determines if it is ok to eat food
# that just felled to the ground.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 11 March 2014


print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")

ys = ""
eat = "Decision: Eat it."
deat = "Decision: Don't eat it."
call = "Decision: Your call."

# Starting point of the decision tree
print("Did anyone see you? (yes/no)")
ys = input()

if ys == "yes":#right side of the decision tree
   print("Was it a boss/lover/parent? (yes/no)")
   ys = input()
   if ys == "yes":
      print("Was it expensive? (yes/no)")
      ys = input()
      if ys == "yes":
         print("Can you cut off the part that touched the floor? (yes/no)")
         ys = input()
         if ys == "yes":
            print(eat)
         else:
            print(call)
      else:
         print("Is it chocolate? (yes/no)")
         ys = input()
         if ys == "yes":
            print(eat)
         else:
            print(deat)
   else:
      print(eat)
else:#left side of the decision tree
   print("Was it sticky? (yes/no)")
   ys = input()
   if ys == "yes":
      print("Is it a raw steak? (yes/no)")
      ys = input()
      if ys == "yes":
         print("Are you a puma? (yes/no)")
         ys = input()
         if ys == "yes":
            print(eat)
         else:
            print(deat)
      else:
         print("Did the cat lick it? (yes/no)")
         ys = input()
         if ys == "yes":
            print("Is your cat healthy? (yes/no)")
            ys = input()
            if ys == "yes":
               print(eat)
            else:
               print(call)
         else:
            print(eat)
   else:
      print("Is it an Emausaurus? (yes/no)")
      ys = input()
      if ys == "yes":
         print("Are you a Megalosaurus? (yes/no)")
         ys = input()
         if ys == "yes":
            print(eat)
         else:
            print(deat)
      else:
         print("Did the cat lick it? (yes/no)")
         ys = input()
         if ys == "yes":
            print("Is your cat healthy? (yes/no)")
            ys = input()
            if ys == "yes":
               print(eat)
            else:
               print(call)
         else:
            print(eat)         



#Sample I/O:

#Welcome to the 30 Second Rule Expert
#------------------------------------
#Answer the following questions by selecting from among the options.
#Did anyone see you? (yes/no)
#yes
#Was it a boss/lover/parent? (yes/no)
#yes
#Was it expensive? (yes/no)
#yes
#Can you cut off the part that touched the floor? (yes/no)
#no
#Decision: Your call.