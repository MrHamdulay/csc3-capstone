#ai program
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
question1 = "Did anyone see you? (yes/no)"
question2 = "Was it a boss/lover/parent? (yes/no)"
question3 = "Was it expensive? (yes/no)"
question4 = "Can you cut off the part that touched the floor? (yes/no)"
question5 = "Is it chocolate? (yes/no)"
question6 = "Was it sticky? (yes/no)"
question7 = "Is it a raw steak? (yes/no)"
question8 = "Is it an Emausaurus? (yes/no)"
question9 = "Did the cat lick it? (yes/no)"
question10 = "Are you a puma? (yes/no)"
question11 = "Are you a Megalosaurus? (yes/no)"
question12 = "Is your cat healthy? (yes/no)"
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
answer1 = ""
answer2 = ""
answer3 = ""
answer4 = ""
answer5 = ""
answer6 = ""
answer7 = ""
answer8 = ""
answer9 = ""
answer10 = ""
answer11 = ""
answer12 = ""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
x = "Decision: Eat it."
y = "Decision: Your call."
z = "Decision: Don't eat it."
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print(question1)
answer1 = input()

if answer1 == "yes":
    print(question2)
    answer2 = input()
if answer1 == "no":
    print(question6)
    answer6 = input()
    
    
if answer2 == "yes":
    print(question3)
    answer3 = input()
if answer2 == "no":
    print(x)
    
    
if answer3 == "yes":
    print(question4)
    answer4 = input()
if answer3 == "no":
    print(question5)
    answer5 = input() 
    

if answer4 == "yes":
    print(x)
if answer4 == "no":
    print(y)


if answer5 == "yes":
    print(x)
if answer5 == "no":
    print(z)  
    
if answer6 == "yes":
    print(question7)
    answer7 = input()
if answer6 == "no":
    print(question8)
    answer8 = input() 
        
if answer7 == "yes":
    print(question10)
    answer10 = input()
if answer7 == "no":
    print(question9)
    answer9 = input() 
    
if answer8 == "yes":
    print(question11)
    answer11 = input()
if answer8 == "no":
    print(question9)
    answer9 = input() 
    
if answer9 == "yes":
    print(question12)
    answer12 = input()
if answer9 == "no":
    print(x) 
    
if answer10 == "yes":
    print(x)
if answer10 == "no":
    print(z) 
    
if answer11 == "yes":
    print(x)
if answer11 == "no":
    print(z)     
    
if answer12 == "yes":
    print(x)
if answer12 == "no":
    print(y)     
    

    
    





    

        
    