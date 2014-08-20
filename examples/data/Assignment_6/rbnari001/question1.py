#Ariel Rubin
#RBNARI001
#23 April 2014
#Program that will right-allign a list of names entered by user

print("Enter strings (end with DONE):")
name = input()

Names  = [] #list of names
longest = 0
count = 0

while(name!="DONE"):
   
   #adding name to the list
    Names.append(name)
    
    if(count > 0): 
        
#finding the longest name in the list
        if(len(Names[count]) > longest):
            longest = len(Names[count])
 
    else:
        longest = len(Names[0])
           
    name = input()
    count = count + 1
   
print("\nRight-aligned list:")   
   
for i in  Names:
   
    print('{:>{x}}'.format(i,x=longest)) #Right allignment
   