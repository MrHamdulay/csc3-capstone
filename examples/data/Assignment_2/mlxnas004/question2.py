# 30 second rule
# nasha meoli
# 7th march 2014
print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")

def again():
    if input("Is your cat healthy? (yes/no)\n") == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Your call.")
 
def puma():
    if input("Are you a puma? (yes/no)\n") == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Don't eat it.")
        
def cat_healthy():
    if input("Did the cat lick it? (yes/no)\n") == "yes":
        again()
    else:
        print("Decision: Eat it.")
    
def mega():
    if input("Are you a Megalosaurus? (yes/no)\n") == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Don't eat it.")

def emau():
    if input("Is it an Emausaurus? (yes/no)\n") == "yes":
        mega()
    else:
        cat_healthy()
        
def steak():
    if input("Is it a raw steak? (yes/no)\n") == "yes":
        puma()        
    else:
        cat_healthy()        
        
        
    
def main_2():
    g = input("Was it sticky? (yes/no)\n")
    if g == "yes":
        steak()
    else:
        emau()



def chocolate():
    if  input("Is it chocolate? (yes/no)\n") == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Don't eat it.")

def cut_off():
    if input("Can you cut off the part that touched the floor? (yes/no)\n") == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Your call.")

def expensive():

    if  input("Was it expensive? (yes/no)\n") == "yes":
        cut_off()
    else:
        chocolate()

def boss():
    
    if input("Was it a boss/lover/parent? (yes/no)\n") == "yes":
        expensive()
    else:
        print("Decision: Eat it.")
        

def main():

    a = input("Did anyone see you? (yes/no)\n")
    if a == "yes":
        boss()
    else:
        main_2()
        

main()






    

                
    