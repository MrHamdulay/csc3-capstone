# 07 March 2014
# Assignment 2
# Jaren Hendricks

# The decision tree program

print ("Welcome to the 30 Second Rule Expert")
print ("-"*36)
print ("Answer the following questions by selecting from among the options.")

# Declaring variables to an empty string
sticky = ""
boss_lover = ""
emausaurus = ""
steak = ""
expensive = ""
cat = ""
puma = ""
mega = ""
chocolate = ""
floor = ""
healthy = ""
see = input("Did anyone see you? (yes/no)\n")

if see == "yes":
    boss_lover = input("Was it a boss/lover/parent? (yes/no)\n")
elif see == "no":
    sticky = input("Was it sticky? (yes/no)\n")
if boss_lover == "yes":
    expensive = input("Was it expensive? (yes/no)\n")
elif boss_lover == "no":
    print ("Decision: Eat it.")
if expensive == "yes":
    floor = input ("Can you cut off the part that touched the floor? (yes/no)\n")
elif expensive == "no":
    chocolate = input ("Is it chocolate? (yes/no)\n")
if chocolate == "yes":
    print ("Decision: Eat it.")
elif chocolate == "no":
    print ("Decision: Don't eat it.")
if floor == "yes":
    print ("Decision: Eat it.")
elif floor == "no":
    print("Decision: Your call.")
if sticky == "yes":
    steak = input ("Is it a raw steak? (yes/no)\n")
elif sticky == "no":
    emausaurus = input ("Is it an Emausaurus? (yes/no)\n")
if steak == "yes":
    puma = input ("Are you a puma? (yes/no)\n")
elif steak == "no":
    cat = input ("Did the cat lick it? (yes/no)\n")
if emausaurus == "yes":
    mega = input("Are you a Megalosaurus? (yes/no) \n")
elif emausaurus == "no":
    cat = input("Did the cat lick it? (yes/no)\n")
if puma == "yes":
    print("Decision: Eat it.")
elif puma == "no":
    print ("Decision: Don't eat it.")
if cat == "yes":
    healthy = input("Is your cat healthy? (yes/no)\n")
elif cat == "no":
    print("Decision: Eat it.")
if healthy == "yes":
    print("Decision: Eat it.")
elif healthy == "no":
    print("Decision: Your call.")
if mega == "yes":
    print("Decision: Eat it.")
elif mega == "no":
    print ("Decision: Don't eat it.")