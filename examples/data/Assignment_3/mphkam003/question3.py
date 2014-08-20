msg= input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))

m=len(msg)
for i in range(thickness):
    print("|"*i + "+" + "-"*m + "-"*(2*(thickness-i)) + "+" + "|"*i) # (thickness-i) decreases by 1 each loop starting from thickness
                                                                     #this is multiplied by 2 because we want to decrease by 2 "-" each loop
for x in range(count):
    print("|"*thickness+" "+msg+" "+"|"*thickness)
    
for l in range(thickness):
    print("|"*(thickness-1) + "+" + "-"*(m) + "-"*(2*l) + "-"*2 + "+" + (thickness-1)*"|")
    thickness-=1
