print("Welcome to the 30 Second Rule Expert ")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
case1=str(input("Did anyone see you? (yes/no)""\n"))
Y=str("yes")
N=str("no")

if case1==Y:
  while Y:
    x= str("yes")
    a=str(input("Was it a boss/lover/parent? (yes/no)""\n"))
    if a==x: 
        b=str(input("Was it expensive? (yes/no)""\n"))
        if b==x:
          c=str(input("Can you cut off the part that touched the floor? (yes/no)""\n"))
          if c==x:
            print("Decision: Eat it.")
            break #end loop
          else:
            print("Decision: Your call.")
            break #end loop
        else:
          d=str(input("Is it chocolate? (yes/no)""\n"))
          if d==x:
            print("Decision: Eat it.")
            break#end loop
          else:
            print("Decision: Don't eat it.")
            break#end loop
    else:
        print("Decision: Eat it.")
        break #exit loop

else:
  while N:
    bake= str("yes")
    eat=str(input("Was it sticky? (yes/no)""\n"))
    if eat==bake:
        cake=str(input("Is it a raw steak? (yes/no)""\n"))
        if cake==bake:
            pj=str(input("Are you a puma? (yes/no)""\n"))
            if pj==bake:
              print("Decision: Eat it.")
              break # end loop
            else:
              print("Decision: Don't eat it.")
              break #end loop
        else:
            cat=str(input("Did the cat lick it? (yes/no)""\n"))
            if cat==bake:
              pen=str(input("Is your cat healthy? (yes/no)""\n"))
              if pen==bake:
                print("Decision: Eat it.")
                break #end loop
              else:
                print("Decision: Your call.")
                break#end loop
            else:
              print("Decision: Eat it.")
              break #end loop
    else:
        muffin=str(input("Is it an Emausaurus? (yes/no)""\n"))
        if muffin==bake:
            sock=str(input("Are you a Megalosaurus? (yes/no)""\n"))
            if sock==bake:
              print("Decision: Eat it.")
              break #end loop
            else:
              print("Decision: Don't eat it.")
              break #end loop
        else:
          lick=str(input("Did the cat lick it? (yes/no)""\n"))
          if lick==bake:
            shhh=str(input("Is your cat healthy? (yes/no)""\n"))
            if shhh==bake:
              print("Decision: Eat it.")
              break#end loop
            else:
              print("Decision: Your call.")
              break#end loop
          else:
            print("Decision: Eat it.")
            break#end loop
             
    
          
           
          
    