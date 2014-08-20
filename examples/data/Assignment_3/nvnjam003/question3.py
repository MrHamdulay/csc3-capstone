message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
for x in range (0, thick):
    print (x*"|" + "+" + (2*thick + len(message) - 2*x)*"-" + "+" + x*"|")
for x in range (0, repeat):
    print (thick*"|" + " " + message + " " + thick*"|")
for x in range (thick-1, -1, -1):
    print (x*"|" + "+" + (2*thick + len(message) - 2*x)*"-" + "+" + x*"|")