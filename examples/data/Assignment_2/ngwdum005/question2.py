#Dumisani Ngwenza
#NGWDUM005
#09/03/14
#This program asks a series of questions that determine if you should eat your food or not after it has fallen onto the ground

print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")

yes = "yes"
no = "no"

ask = input ("Did anyone see you? (yes/no)\n")
if ask.lower()=="yes":
    observer = input ("Was it a boss/lover/parent? (yes/no)\n")
    if observer.lower()=="yes":
        pricey = input ("Was it expensive? (yes/no)\n")
        if pricey.lower()=="yes":
            removable = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if removable.lower()=="no":
                print ("Decision: Your call.")
            else:
                print ("Decision: Eat it.")
        else:
            flavour = input ("Is it chocolate? (yes/no)\n")
            if flavour.lower()=="no":
                print ("Decision: Don't eat it.")
            else:
                print ("Decision: Eat it.")
    else:
        print ("Decision: Eat it.")
else:
    sticky = input ("Was it sticky? (yes/no)\n")
    if sticky.lower()=="yes":
        raw_steak = input ("Is it a raw steak? (yes/no)\n")
        if raw_steak.lower()=="yes":
            pumaQ = input ("Are you a puma? (yes/no)\n")
            if pumaQ.lower()=="yes":
                print ("Decision: Eat it.")
            else:
                print ("Decision: Don't eat it.")
        else:
            cat = input ("Did the cat lick it? (yes/no)\n")
            if cat.lower()=="yes":
                health = input ("Is your cat healthy? (yes/no)\n")
                if health.lower()=="yes":
                    print ("Decision: Eat it.")
                else:
                    print ("Decision: Your call.")
            else:
                print ("Decision: Eat it.")
    else:
        weird = input ("Is it an Emausaurus? (yes/no)\n")
        if weird.lower()=="yes":
            Even_Weird = input ("Are you a Megalosaurus? (yes/no)\n")
            if Even_Weird.lower()=="yes":
                print ("Decision: Eat it.")
            else:
                print ("Decision: Don't eat it.")
        else:
            catB = input ("Did the cat lick it? (yes/no)\n")
            if catB.lower()=="yes":
                healthy_again = input ("Is your cat healthy? (yes/no)\n")
                if healthy_again.lower()=="yes":
                    print ("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print ("Decision: Eat it.")