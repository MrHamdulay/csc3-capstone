#30 Second rule expert
#Tayla George
#11 March 2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

yes= "yes"
no = "no"
decision="Decision: Eat it"

q1=input("Did anyone see you? (yes/no)\n")
if q1=='yes':
  q2= input("Was it a boss/lover/parent? (yes/no)\n")
  if q2=='yes':
    q3=input("Was it expensive? (yes/no)\n")  
    if q3=='yes':
      q4=input("Can you cut off the part that touched the floor? (yes/no)\n")
      if q4=='no':
            print("Decision: Your call.")
      elif q4=='yes':
        print("Decision: Eat it.")
       
    elif q3=='no':
          q5=input("Is it chocolate? (yes/no)\n")  
          if q5=='yes':
                print("Decision: Eat it.") 
          elif q5=='no':
                  print("Decision: Don't eat it.")    
  elif q2=='no':
    print("Decision: Eat it.")   
elif q1=='no':
  q6= input("Was it sticky? (yes/no)\n")
  if q6=='yes':
    q7= input("Is it a raw steak? (yes/no)\n")
    if q7=='yes':
      q8= input("Are you a puma? (yes/no)\n")
      if q8=='no':
        print("Decision: Don't eat it.")
      elif q8=='yes':
        print("Decision: Eat it.")
    elif q7=='no':
      q9=input("Did the cat lick it? (yes/no)\n")
      if q9=='no':
        print("Decision: Eat it.")
      elif q9=='yes':
        q10=input("Is your cat healthy? (yes/no)\n")
        if q10=='yes':
          print("Decision: Eat it.")
        elif q10=='no':
          print("Decision: Your call.")
  elif q6=='no':
    q11=input("Is it an Emausaurus? (yes/no)\n")
    if q11=='yes':
      q12=input("Are you a Megalosaurus? (yes/no)\n")
      if q12=='yes':
        print("Decision: Eat it.")
      elif q12=='no':
        print("Decision: Don't eat it.")
    elif q11=='no':
      q9=input("Did the cat lick it? (yes/no)\n")
      if q9=='no':
        print("Decision: Eat it.")
      elif q9=='yes':
        q10=input("Is your cat healthy? (yes/no)\n")
        if q10=='yes':
          print("Decision: Eat it.")
        elif q10=='no':
          print("Decision: Your call.")
        
      
   
    