#22 March 2014
#Assignment 3
#LYLJON002

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))


thickness2=0
thickness2=thickness
line=0
line2=thickness


while thickness > 0:
    print("|"*line+"+"+("-"*len(message))+"-"*((thickness-1)*2)+"--"+"+"+"|"*line)
    thickness-=1
    line+=1
while repeat>0:
    print(("|"*(thickness2)+ " "+message+" "+"|"*(thickness2)))
    repeat-=1
dash=0
while thickness2 > 0:
    print((line2-1)*"|"+"+"+(len(message)*"-")+("-"*dash)+"--"+"+"+(line2-1)*"|")
    dash+=2
    thickness2-=1
    line2-=1  
