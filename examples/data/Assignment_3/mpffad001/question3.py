def frame():
    mess=input("Enter the message:" '\n')
    x=eval(input("Enter the message repeat count:" '\n'))
    y=eval(input("Enter the frame thickness:" '\n'))
    length=len(mess)+(2*y)
    character=0
    for i in range (y):
        print(character*"|","+","-"*length,"+", character*"|",sep="")
        character+=1
        length-=2
    for j in range (x):
        print(y*"|"," ",mess, " ",y*"|",sep="")
    length+=2
    character-=1
    for k in range (y):
        print(character*"|","+","-"*length,"+", character*"|",sep="")
        length+=2
        character-=1        
    
  


frame()
