"""Program to right align list
Micaela Narasmulu
25 April 2014"""

s=[] 

print("Enter strings (end with DONE):") 

x=""
while x!= "DONE":  
    x=input() 
    s.append(x)
s.remove("DONE")


maxLength=0 
for i in  range(len(s)): 
    if(len(s[i])>maxLength): 
        maxLength=len(s[i])
    else:
        maxLength=maxLength
        
print()
print("Right-aligned list:")
for i  in range(len(s)): 
    spaces= maxLength-len(s[i])
    print(" "*spaces+s[i])