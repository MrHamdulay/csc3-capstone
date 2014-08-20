#the 30 sec test for food
print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
check = input("Did anyone see you? (yes/no)\n")
if(check =="yes"):
    check = input("Was it a boss/lover/parent? (yes/no)\n")
    if(check=="no"):
        print("Decision: Eat it.")
    elif(check=="yes"):
        check = input("Was it expensive? (yes/no)\n")
        if(check =="yes"):
            check = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(check == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")

        else:
            check=input("Is it chocolate? (yes/no)\n")
            if(check == "yes"):
                print("Decision: Don't eat it.")
            else:
                print("Decision: Don't eat it.")
else:
    check = input("Was it sticky? (yes/no)\n")
    if(check == "yes"):
        check = input("Is it a raw steak? (yes/no)\n")
        if(check == "yes"):
            check = input("Are you a puma? (yes/no)\n")  
            if(check== "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            check=input("Did the cat lick it? (yes/no)\n")
            if(check == "no"):
                print("Decision: Eat it.")
            else:
                check=input("Is your cat healthy? (yes/no)\n")
                if(check == "yes"):
                    print("Decision: Eat it.")
                else:
                       print("Decision: Your Call.")            
           
   # elif(check=="no"):
        #check=input("Did the cat lick it? (yes/no)\n")
       # if(check == "no"):
        #    print("Decision: Eat it.")
        #else:
            #check=input("Is your cat healthy? (yes/no)\n")
            #if(check == "yes"):
                #print("Decision: Eat it.")
            #else:
               # print("Decision: Your Call.")   #      
            
    else:
        check = input("Is it an Emausaurus? (yes/no)\n") 
        if(check == "no"):
            check=input("Did the cat lick it? (yes/no)\n")
            if(check == "no"):
                print("Decision: Eat it.")
            else:
                check=input("Is your cat healthy? (yes/no)\n")
                if(check == "yes"):
                    print("Decision: Eat it.")
                elif(check== 'no'):
                    print("Decision: Your Call.")
          
        elif(check== 'yes'):
            check=input("Are you a Megalosaurus? (yes/no)\n")
            if(check == "yes"):
                print("Decision: Eat it.")
            elif(check=='no'):
                print("Decision: Your Call.")
                          

                