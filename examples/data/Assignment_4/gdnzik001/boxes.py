#Zikho Godana
#31 March 2014
#Program to write a python module that contains 3 functions to create hollow boxes of stars

def print_square():
    for i in range(5):
        if i==0 or i==4:
            print("*"*5)
        else:
            print("*"," "*3,"*",sep="")
        
def print_rectangle(width,height):
    gap=width-2
    for j in range(height):
        if j==0 or j==height-1:
            print("*"*width)
        else:
            print("*"," "*abs(gap),"*",sep="")

def get_rectangle(width,height):
    gap=width-2
    line1=""
    line3=""
    for k in range(height):
        if k==0:
            line1 =line1+"*"*width 
        else:
            line2 = ("*" + " "*abs(gap)+"*"+"\n")*(height-2)
            line3 = line1 + "\n"+ str (line2)+line1
    return line3     
        
    
