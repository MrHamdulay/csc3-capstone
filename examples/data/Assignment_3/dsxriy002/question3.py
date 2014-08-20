#Riya Desai
#Question 3 - Assignment 3
#24 March 2014
 
 
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
for top in range (0,(repeat+thickness)):
            if((thickness-1)<top<(thickness+repeat)):
                        print("|"*thickness,message,"|"*thickness)
            else:
                        print('|'*top + "+" + "-"*(len(message)+2 + (thickness-1)*2 - top*2) + "+" + "|"*top)

for bottom in range((thickness-1),-1,-1):
            if(bottom==0):
                        print("+" + "-"*(len(message)+2 + (thickness-1)*2 - bottom*2) + "+")
            else:
                        print('|'*bottom + "+" + "-"*(len(message)+2 + (thickness-1)*2 - bottom*2) + "+" + "|"*bottom) 