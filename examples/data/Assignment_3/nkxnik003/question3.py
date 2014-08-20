#Nikhil Jiten Naik
#Question 3 - Assignment 3
#24 March 2014
 
 
mess = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
for top in range (0,(rep+thick)):
            if((thick-1)<top<(thick+rep)):
                        print("|"*thick,mess,"|"*thick)
            else:
                        print('|'*top + "+" + "-"*(len(mess)+2 + (thick-1)*2 - top*2) + "+" + "|"*top)

for bottom in range((thick-1),-1,-1):
            if(bottom==0):
                        print("+" + "-"*(len(mess)+2 + (thick-1)*2 - bottom*2) + "+")
            else:
                        print('|'*bottom + "+" + "-"*(len(mess)+2 + (thick-1)*2 - bottom*2) + "+" + "|"*bottom) 