"""Amy Bosworth, Assignment 6, Question 1, 20 April 2014"""

#Get inputs
name= input("Enter strings (end with DONE):\n")
names=[]

#Put inputs into a list
while name!='DONE':
    names.append(name)
    name=input()
    
#Iterate through list changing each input into its length of input and then storing as another list
length=[] 
for i in names:
    lengths=len(i)  
    length.append(lengths)

#find max length
if length==[]:
    longest=''
else:
    longest=max(length)


#loop to align list with max 
print("\nRight-aligned list:")
for j in names:
    spaces=longest-len(j)
    
    if spaces!=0:
        print(spaces*' ',j,sep='')
    else:
        print(j)
    
    
    
    
    
