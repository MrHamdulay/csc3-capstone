msg = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
w = len(msg)+(thick*2)+2
d = w-4

if rpt>0 and thick>0:    
    print("+" + ("-"*(w-2)) + "+")  

for i in range(thick-1):    
    print("|"*(i+1)+"+" + ("-"*(d-(i*2))) + "+" +"|"*(i+1))    

for r in range(rpt):
    print("|"*thick, msg, "|"*thick)
    
for i in range(thick-1, 0, -1):    
    print("|"*(i)+"+" + ("-"*((d+2)-(i*2))) + "+" +"|"*(i))
    
if rpt>0 and thick>0:    
    print("+" + ("-"*(w-2)) + "+")  