# Program to right-allign list of names entered by user
# Brandon Hall (HLLBRA005)
# 25/04/2014

print("Enter strings (end with DONE):")
name = input()

LNames  = [] #list of names
longest = 0
count = 0

while(name!="DONE"):
   
    LNames.append(name)
    
    if(count > 0): 
        
        if(len(LNames[count]) > longest):
            longest = len(LNames[count])
 
    else:
        longest = len(LNames[0])
           
    name = input()
    count = count + 1
   
print("\nRight-aligned list:")   
   
for i in  LNames:
   
    print('{:>{x}}'.format(i,x=longest)) #Right allignment
   