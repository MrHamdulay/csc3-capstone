print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

eat = ("Decision: Eat it.")
d_eat = ("Decision: Don't eat it.")
callit = ("Decision: Your call.")

yes = 1
no = 2

see=eval(input("Did anyone see you? (yes/no)\n"))
if see == 1  :
  lover = eval(input("Was it a boss/lover/parent? (yes/no)\n"))
  if lover == 1:
    ex = eval(input("Was it expensive? (yes/no)\n"))
    if ex== 1:
      cut = eval(input("Can you cut off the part that touched the floor? (yes/no)\n"))
      if cut == 1:
        print(eat)
      else : print(callit) 
    else :  
      choc = eval(input("Is it chocolate? (yes/no)\n"))
      if choc == 1:
        print(eat)
      else: print(d_eat)
  else:print(eat)
  
else: 
  sticky = eval(input("Was it sticky? (yes/no)\n"))
  if sticky == 1 :
    steak = eval(input("Is it a raw steak? (yes/no)\n"))
    if steak == 1:
      puma = eval(input("Are you a puma? (yes/no)\n"))
      if puma == 2:
        print(d_eat)
      else: print(eat)
    else:
      lick = eval(input("Did the cat lick it? (yes/no)\n"))
      if lick == 1 : 
        health = eval(input("Is your cat healthy? (yes/no)\n"))
        if health == 1 : print(eat)
        else: print(callit)
      else: print(eat)
  else:
    ema = eval(input("Is it an Emausaurus? (yes/no)\n"))
    if ema==2:
      lick = eval(input('Did the cat lick it? (yes/no)\n'))
      if lick == 1:
          health = eval(input('Is your cat healthy? (yes/no)\n'))
          if health==1: print(eat)
          else: print(callit)
      else: print(eat)  
    else:
        mega = eval(input('Are you a Megalosaurus? (yes/no)\n'))
        if mega==1:
          print(eat)
        else: 
          print(d_eat)             

  
  