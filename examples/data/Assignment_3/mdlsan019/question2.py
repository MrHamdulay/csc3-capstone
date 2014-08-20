#Sanele Mdlalose
#MDLSAN019
#question2

h=eval(input("Enter the height of the triangle:\n"))
space=(h-1)
char=1
while char<=2*h:
    print(" "*space,end='')
    print(char*"*")
    char+=2
    space-=1