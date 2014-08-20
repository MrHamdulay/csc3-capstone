#GLMSUM001
#Sumayah Goolam Rassool
#23 april 2014

#-----------------------------------creating empty array

array=[]

#------------------------------------allow user to enter names into the array

name=input("Enter strings (end with DONE):\n")

if name=="DONE":
    print("")
    print("Right-aligned list:")
else:
    while name!="DONE":
        array.append(name)
        name=input()

#------------------------------------store length of names in another array

    width=[]

    arraylength=len(array)

    for i in range (arraylength):
    
        namelength=len(array[i])
        
        width.append(namelength)
    
    width.sort()
    end=len(width)



#------------------------------------set width equal to maximum length
    max_width=width[end-1]
#------------------------------------output right alligned list using format
    print("")
    print("Right-aligned list:")

    for j in range (arraylength):
    
        space=max_width-(len(array[j]))
        print(" "*space,array[j],sep="")
        
