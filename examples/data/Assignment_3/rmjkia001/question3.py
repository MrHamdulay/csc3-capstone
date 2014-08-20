m = input("Enter the message:\n")
r = eval(input("Enter the message repeat count:\n"))
t = eval(input("Enter the frame thickness:\n"))
for top in range (0,(r+t)):
            if((t-1)<top<(t+r)):
                        print("|"*t,m,"|"*t)
            else:
                        print('|'*top + "+" + "-"*(len(m)+2 + (t-1)*2 - top*2) + "+" + "|"*top)

for bottom in range((t-1),-1,-1):
            if(bottom==0):
                        print("+" + "-"*(len(m)+2 + (t-1)*2 - bottom*2) + "+")
            else:
                        print('|'*bottom + "+" + "-"*(len(m)+2 + (t-1)*2 - bottom*2) + "+" + "|"*bottom)
                        