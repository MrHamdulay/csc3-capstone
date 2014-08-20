#Sphiwe Muthembi
#Student number: MTHSPH007
#date: 12/03/2014


#first output
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

result_eatit= "Eat it."
result_donteat= "Don't eat it. "
result_youcall= "Your call."

#dropped food test
#Function Catlick
def catlick():
     cat= input("Did the cat lick it? (yes/no)\n")
     if cat== "no":
          print("Decision:",result_eatit)
     elif cat== "yes":
          health= input("Is your cat healthy? (yes/no)\n")
          if health== "yes":
               print("Decision:",result_eatit)
          elif health== "no":
               print("Decision:",result_youcall)
               
yes= "yes"
no= "no"
see= input("Did anyone see you? (yes/no)\n")
#==========================yes Section===================================
if see== yes:
     q1= input("Was it a boss/lover/parent? (yes/no)\n")
     if q1== yes :
          expensive= input("Was it expensive? (yes/no)\n")
          if expensive== no:
               choc= input("Is it chocolate? (yes/no)\n")
               if choc== yes:
                    print("Decision:",result_eatit)
               elif choc== no:
                    print("Decision:",result_donteat)
          elif expensive== yes:
               cut= input("Can you cut off the part that touched the floor? (yes/no)\n")
               if cut== no:
                    print("Decision:",result_youcall)
               elif cut== yes:
                    print("Decision:",result_eatit)
     elif q1== no:
          print("Decision:",result_eatit)
#=========================no Section=====================================
elif see== no:
     sticky= input("Was it sticky? (yes/no)\n")
     if sticky== yes:
          steak= input("Is it a raw steak? (yes/no)\n")
          if steak== no:
               catlick()
          elif steak== yes:
               puma= input("Are you a puma? (yes/no)\n")
               if puma== yes:
                    print("Decision:",result_eatit)
               elif puma== no:
                    print("Decision:",result_donteat)
          
          #=================================================
     elif sticky== no:
          emasasaurus= input("Is it an Emausaurus? (yes/no)\n")
          if emasasaurus== no:
               catlick()
          elif emasasaurus== yes:
               mag= input("Are you a Megalosaurus? (yes/no)\n")
               if mag== yes:
                    print("Decision:",result_eatit)
               elif mag== no:
                    print("Decision:",result_donteat)

#================================end of code============================