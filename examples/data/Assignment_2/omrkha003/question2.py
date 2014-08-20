# program to determine whether or not you should eat food that fell on the ground
# by: khadeejah omar
# 7 march 2014

print("Welcome to the 30 Second Rule Expert\n"+"-"*36) # greeting
print("Answer the following questions by selecting from among the options.")

def cat(): 
           cat = input("Did the cat lick it? (yes/no)\n")
           if cat == "no" : # if cat didn't lick it
                      print("Decision: Eat it.")
           else: # if cat licked it
                      health = input("Is your cat healthy? (yes/no)\n")
                      if health == "yes" : # if cat is healthy
                                 print("Decision: Eat it.")
                      else : # if cat is unhealthy
                                 print("Decision: Your call.")


anyone_see = input("Did anyone see you? (yes/no)\n")

if anyone_see == "yes" : # if somebody saw
           who = input("Was it a boss/lover/parent? (yes/no)\n")
           if who == "no" :
                      print("Decision: Eat it.")
           else : # if person who saw was boss/lover/parent
                      price = input("Was it expensive? (yes/no)\n")
                      if price == "yes" : # if expensive
                                 cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
                                 if cut == "yes" : # if it can be cut off
                                            print("Decision: Eat it.")
                                 else : # if it can't be cut off
                                            print("Decision: Your call.")
                      else : # if inexpensive
                                 chocolate = input("Is it chocolate? (yes/no)\n")
                                 if chocolate == "yes" : # if it is chocolate
                                            print("Decision: Eat it.")
                                 else: # if it isn't chocolate
                                            print("Decision: Don't eat it.")

else : # if nobody saw
           sticky = input("Was it sticky? (yes/no)\n")
           if sticky == "yes" : # if food was sticky
                      raw_steak = input("Is it a raw steak? (yes/no)\n")
                      if raw_steak == "yes" : # if it was raw steak
                                 puma = input("Are you a puma? (yes/no)\n")
                                 if puma == "yes" : # if you are a puma
                                            print("Decision: Eat it.")
                                 else : # if you aren't a puma
                                            print("Decision: Don't eat it.")
                      else : # if it wasn't raw steak
                                 cat()
           else : # if food wasn't sticky
                      emausaurus = input("Is it an Emausaurus? (yes/no)\n")
                      if emausaurus == "no" : # if it is an emausaurus
                                 cat()
                      else: # if it is an emausaurus
                                 megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                                 if megalosaurus == "yes" : # if you are a megalosaurus
                                            print("Decision: Eat it.")
                                 else : # if you aren't a megalosaurus
                                            print("Decision: Don't eat it.")