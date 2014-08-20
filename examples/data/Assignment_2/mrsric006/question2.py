#Creator Richard Marais

def cupcake():
   print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")    #opening text
   
   if (input("Did anyone see you? (yes/no)\n") == "yes"):                     # conditions of the decision tree begin
      if(input("Was it a boss/lover/parent? (yes/no)\n") == "yes"):
         if(input("Was it expensive? (yes/no)\n") =="yes"):
            if(input("Can you cut off the part that touched the floor? (yes/no)\n") == "yes"):
               print("Decision: Eat it.") 
            else:
               print("Decision: Your call.")
         else:
            if(input("Is it chocolate? (yes/no)\n") == "yes"):
               print("Decision: Eat it.")   
            else:
               print("Decision: Don't eat it.")
      else: 
         print("Decision: Eat it.")         
   else: 
      if(input("Was it sticky? (yes/no)\n") == "yes"):
         if(input("Is it a raw steak? (yes/no)\n") == "yes"):
            if(input("Are you a puma? (yes/no)\n") == "yes"):
               print("Decision: Eat it.")
            else:
               print("Decision: Don't eat it.")
         else:
            if(input("Did the cat lick it? (yes/no)\n") == "yes"):
               if(input("Is your cat healthy? (yes/no)\n") == "yes"):
                  print("Decision: Eat it.")
               else:
                  print("Decision: Your call.")
            else:
               print("Decision: Eat it.")
      else:
         if(input("Is it an Emausaurus? (yes/no)\n") == "yes"):
            if(input("Are you a Megalosaurus? (yes/no)\n") == "yes"):
               print("Decision: Eat it.")
            else:
               print("Decision: Don't eat it.")
         else:   
            if(input("Did the cat lick it? (yes/no)\n") == "yes"):
               if(input("Is your cat healthy? (yes/no)\n") == "yes"):
                  print("Decision: Eat it.")
               else:
                  print("Decision: Your call.")
            else:
               print("Decision: Eat it.")                  # decision tress conditions end
   
cupcake()
            
     
              
               
            
            