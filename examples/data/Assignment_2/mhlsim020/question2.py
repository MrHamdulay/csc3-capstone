# A program to illustrate a decision tree.
#Simlindile Mahlaba
#14 March 2014
ans="yes"

print(input("Did anyone see you? (yes/no)\n"))
if("yes"):
        print(input("Was it a boss/lover/parent? (yes/no)\n")
              if("yes"):
                print(input("Was it expensive? (yes/no)\n"))
                if("yes"):
                        print(input("Can you cut off the part that touched the floor? (yes/no)\n"))
                        if("yes"):
                                print("Decision: Your call.")
                        else:
                                print("EAT IT.")
                else:
                        print("EAT IT.")
        else:
                print("Decision: Your call.")
else:
        print("EAT IT.")
        

