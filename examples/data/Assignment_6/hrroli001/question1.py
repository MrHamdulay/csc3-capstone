# Question 1 - Assignment 6
# Oliver Harrison
# 21 April 2014


# Get names and add to list
namelist=[]              # Create empty list

name=input("Enter strings (end with DONE):\n")
while name != "DONE":
    namelist.append(name)
    name=input("")
    
# Determine largest length

maxlength=0

for name in namelist:
    if len(name)>maxlength:
        maxlength = len(name)
    else:
        continue
    
# format and print
print("")
print("Right-aligned list:")
        
for name in namelist:
    formatter = '{0:>'+str(maxlength)+'}'
    #name_new = '{0:<'+str(maxlength)+'}'.format(maxlength, name)
    print (formatter.format(name))
    


