# Michaela Heale
# Assignment 3 Question 3

msg = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
thk = eval(input("Enter the frame thickness:\n"))

msg = " "+msg+" "
lng = int(len(msg))
top = ""
mdl = ""
btm = ""

#CountVariables for x i.e. the top
s = thk-1
b = 0
for x in range(thk,0,-1):
    #ConstructingTop
    top += ("|"*b)+"+"+(("-")*(lng+(2*s)))+"+"+("|"*b)+"\n"
    s -= 1
    b +=1

#CountVariables for y i.e. the bottom
s = 0 
b = thk-1
for y in range(0,thk,1):
    #ConstructingBottom
    btm += ("|"*b)+"+"+(("-")*(lng+(2*s)))+"+"+("|"*b)+"\n"
    b -= 1
    s += 1
    
for z in range(rpt):
    #ConstructingMiddle
    top += ("|"*thk)+msg+("|"*thk)+"\n"
    
print(top,mdl,btm,sep="")
    