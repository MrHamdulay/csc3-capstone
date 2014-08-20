message = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
for i in range(thickness):
    dashes = "-"*(len(message)+(2*thickness)-(i*2))
    print("|"*i+"+" + dashes + "+"+i*"|")
for j in range(count):
    print("|"*(i+1)+" "+ message +" " + (i+1)*"|")
for i in range(thickness-1,-1,-1):
    dashes = "-"*(len(message)+(2*thickness)-(i*2))
    print("|"*i+"+" + dashes + "+"+i*"|")    
    