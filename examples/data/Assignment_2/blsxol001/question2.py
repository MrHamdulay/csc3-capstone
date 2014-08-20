# a program to help you decide whether you should eat food you've dropped on floor
# xola bilose
# 10/03/2014
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
decision = input("Did anyone see you? (yes/no)\n")
if decision == 'yes':
  decision1 = input("Was it a boss/lover/parent? (yes/no)\n")
  if decision1 == 'no':
    print ("Decision: Eat it.")
  else :
    decision1_1 = input( "Was it expensive? (yes/no)\n")
    if decision1_1 == 'yes': 
      decision1_1a = input("Can you cut off the part that touched the floor? (yes/no)\n")
      if decision1_1a == 'yes':
        print("Decision: Eat it.")
      else:
        print("Decision: Your call.")
    else:
      decision1_1b = input("Is it chocolate? (yes/no)\n")
      if decision1_1b == 'yes':
        print("Decision: Eat it.")
      else:
        print("Decision: Don't eat it.")
else:
  decision2 = input("Was it sticky? (yes/no)\n")
  if decision2 == 'yes':
    decision2_1 = input("Is it a raw steak? (yes/no)\n")
    if decision2_1 == 'yes':
      decision2_1a = input("Are you a puma? (yes/no)\n")
      if decision2_1a == 'yes':
        print("Decision: Eat it.")
      else:
        print("Decision: Don't eat it.")
    else:
      decision2_1b = input("Did the cat lick it? (yes/no)\n")
      if decision2_1b  == 'no':
        print("Decision: Eat it.")
      else:
        decision2_1bb = input("Is your cat healthy? (yes/no)\n")
        if decision2_1bb == 'yes':
          print("Decision: Eat it.")
        else :
          print("Decision: Your call.")
  else:
      decision2_2 = input ("Is it an Emausaurus? (yes/no)\n")
      if decision2_2 == 'yes':
        decision2_2a = input("Are you a Megalosaurus? (yes/no)\n")
        if decision2_2a == 'yes':
          print("Decision: Eat it.")
        else:
          print("Decision: Don't eat it.") 
      else:
        decision2_2b = input("Did the cat lick it? (yes/no)\n")
        if decision2_2b == 'yes':
          decision2_2ba = input("Is your cat healthy? (yes/no)\n")
          if decision2_2ba == 'yes':
            print("Decision: Eat it.")
          else: print("Decision: Your call.")
        else:
          print("Decision: Eat it.")