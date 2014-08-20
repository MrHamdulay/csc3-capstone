message = input("Enter the message:\n")
msgCount= eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
interior = " " + message + " "
width = thickness + (len(interior)) + thickness
height = (thickness*2) + msgCount

for i in range(0, thickness):
    l = "|"*i
    lCount = len(l)
    dashCount = width-(lCount*2)-2
    string1 = l + "+" + ("-"*dashCount) + "+" + l
    print(string1)
    
for j in range(msgCount):
    outputstring = ("|"*thickness) + interior + ("|"*thickness)
    print(outputstring)
    
for k in range(thickness,0,-1):
    l = "|"*(k-1)
    lNum = len(l) 
    dashNum = width - (lNum*2) -2
    string2 = l + "+" + ("-"*dashNum) + "+" + l
    print(string2)