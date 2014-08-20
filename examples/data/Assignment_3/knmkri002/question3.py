# Frame drawer
# Kristin Kinmont
# 21 March 2014

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
n = len(message)
k = 0
for i in range(thick,0,-1):
    x=n+2*i
    corner1 ='|'*(k)+'+'
    corner2 = '+'+ '|'*(k)
    print(corner1 +'-'*(x)+ corner2)
    k+=1
for j in range(repeat):
    print('|'*thick,message,'|'*thick)
k= thick-1
for i in range(1,thick+1):
    x=n+2*i
    corner1 ='|'*(k)+'+'
    corner2 = '+'+ '|'*(k)
    print(corner1 +'-'*(x)+ corner2)
    k-=1
    