s=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
thick2=thickness//2
def Tborder(thickness):
    for i in range(thick2):
        print("+","-"*(len(s)+len(s)//2),"+",sep="")
        print("|","+","-"*(len(s)+len(s)//4),"+","|",sep="")

def TopBorder(thickness):
    c=0
    for i in range(thickness):
        print("|"*c,"+","-"*(len(s)+(thickness*2)-2*c),"+","|"*c,sep="")
        c+=1
TopBorder(thickness)
for i in range(count):
    print("|"*thickness,s,"|"*thickness,sep=" ") 

def BotBorder(thickness):
    c=thickness-1
    for i in range(thickness):
        print("|"*c,"+","-"*(len(s)+(thickness*2)-2*c),"+","|"*c,sep="")
        c-=1        
        

BotBorder(thickness)