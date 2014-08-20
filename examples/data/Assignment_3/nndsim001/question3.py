# This program prints a message enclosed in a frame made with characters +,-,|

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 25 March 2014


message = input("Enter the message:\n")

repeat = eval(input("Enter the message repeat count:\n"))

thickness = eval(input("Enter the frame thickness:\n"))

#This part prints the frame based on the inputs supplied above

length = len(message)
lenthick = length + thickness + thickness

msglen = len(message)+2+2*thickness
dass = lenthick - 2 
ley = thickness - 1

# This nested loops print the top horizontal boundary
for o in [1]:
    if thickness != 0:  
        print("{p}{d}{p}".format(p="+",d="-"*(lenthick)))    
    for i in range(thickness-1):
        print("{l}".format(l="|"*(thickness - ley)),end='')
        print("{p}{d}{p}".format(p="+",d="-"*dass),end='')
        print("{l}".format(l="|"*(thickness - ley)))
        if dass<(length + 3):
            dass = length + 3
        else:
            dass = dass - 2
        ley = ley - 1

# This loop prints the middle lines including the message       
if repeat != 0:
    for j in range(repeat):
        printchr = "{wall}{spc}{mess}{spc}{wall}"
        print(printchr.format(wall="|"*thickness,mess=message,spc=" "))

# This nested loops prints the bottom horizontal boundary
dass = length + 2
ley = thickness - (thickness - 1)
for b in range(thickness - 1):    
    print("{l}".format(l="|"*(thickness - ley)),end='')
    print("{p}{d}{p}".format(p="+",d="-"*dass),end='')
    print("{l}".format(l="|"*(thickness - ley)))  
    ley = ley + 1
    dass = dass + 2
       
# This line prints the outside bottom horizontal boundary    
if thickness !=0:
    print("{p}{d}{p}".format(p="+",d="-"*(lenthick))) 

#Sample I/O:

#Enter the message:
#Hello World
#Enter the message repeat count:
#3
#Enter the frame thickness:
#+---------------+
#|+-------------+|
#|| Hello World ||
#|| Hello World ||
#|| Hello World ||
#|+-------------+|
#+---------------+