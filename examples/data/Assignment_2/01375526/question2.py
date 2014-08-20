print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
ans = input ("Did anyone see you? (yes/no)\n")
if (ans == "yes"):
    ans = input ("Was it a boss/lover/parent? (yes/no)\n")
    if (ans == "yes"):
        ans = input ("Was it expensive? (yes/no)\n")
        if (ans == "yes"):
            ans = input ("Can you cut off the part that touched the floor? (yes/no)\n")
            if (ans == "yes"):
                print ("Decision: Eat it.\n")
            else:
                print ("Decision: Your call.\n")
        else:
            ans = input ("Is it chocolate? (yes/no)\n")
            if (ans == "yes"):
                print ("Decision: Eat it.\n")
            else:
                print ("Decision: Don't eat it.\n")
    else:
       print ("Decision: Eat it.\n")
else:
    ans = input ("Was it sticky? (yes/no)\n")
    if (ans == "yes"):
        ans = input ("Is it a raw steak? (yes/no)\n")
        if (ans == "yes"):
            ans = input ("Are you a puma? (yes/no)\n")
            if (ans == "yes"):
                print ("Decision: Eat it.\n")
            else:
                print ("Decision: Don't eat it.\n")
        else:
            ans = input ("Did the cat lick it? (yes/no)\n")
            if (ans == "yes"):
                ans = input ("Is your cat healthy? (yes/no)\n")
                if (ans == "yes"):
                    print ("Decision: Eat it.\n")
                else:
                    print ("Decision: Your call.\n")
            else:
                print ("Decision: Eat it.\n")
    else:            
       ans = input ("Is it an Emausaurus? (yes/no)\n")
       if (ans == "yes"):
           ans = input ("Are you a Megalosaurus? (yes/no)\n")
           if (ans == "yes"):
               print ("Decision: Eat it.\n")
           else:
               print ("Decision: Don't eat it.\n")
       else:        
           ans = input ("Did the cat lick it? (yes/no)\n")
           if (ans == "yes"):
               ans = input ("Is your cat healthy? (yes/no)\n")
               if (ans == "yes"):
                   print ("Decision: Eat it.\n")
               else:
                   print ("Decision: Your call.\n")
           else:
               print ("Decision: Eat it.\n")
