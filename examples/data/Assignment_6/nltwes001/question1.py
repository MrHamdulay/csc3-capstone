#ASSIGNMENT 6
#NLTWES001
#QUESTION 1

#create list
print("Enter strings (end with DONE):")
max=0          #length of longest string
i=0
slist=[]        #string list
while (True):
    s=input()   #string variable
    if s=="DONE":
        print()
        print("Right-aligned list:")
        for k in range(len(slist)):
            print(slist[k].rjust(max))
        break       
    else:
        if len(s)>max:
            max=len(s)
        slist.append(s)
    