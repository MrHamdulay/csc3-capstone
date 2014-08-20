"""counting pairs
Sachin Murugan
9/5/2014"""
Message = input("Enter a message:\n")

def RepeatedCharacter (Message, y):
#base case to check for one letter or no letters   
    if len(Message)==0 or len(Message)==1:
        return print("Number of pairs:", y)
   
    elif Message[0] == Message[1]:
        y+=1
        return RepeatedCharacter(Message[2:],y) #check pairs for every 2 characters
    

    else:
        return RepeatedCharacter(Message[2:],y)#and then move on to next two characters

RepeatedCharacter(Message,0)



        