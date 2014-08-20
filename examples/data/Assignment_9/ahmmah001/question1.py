def student_analysis(f1):
    f=open(f1,"r")
    f=f.read()
    f=f.split("\n")
    l=[]
    l2=[]
    list0=[]
    add=0
    salm=0
    empt=""
    for i in f:
        l2.append(i)
        for j in l2:
            c=j.split(",")
            d=c[1]
        add=add+int(d)
    s=add
   
       
     
        
        
        
    #for i in range(len(f)):
        #pos=f[i]
        #pos=pos.split(",")
        #add=add + int(pos[1])
        #l.append(add)
        #for j in l:
            #l1=len(l)-1
    #list0.append(l[l1])
     
           
    average=(s/len(f))
    for i in range(len(f)):
        pos=f[i]
        pos=pos.split(",")
        salm=salm + (eval(pos[1]) - average)**2
        
    std_dev= (salm/len(f))**0.5
            
    print("The average is:", "{0:1.2f}".format(average))
    print("The std deviation is:","{0:1.2f}".format(std_dev))
    
    one_less= average - std_dev
    for i in range(len(f)):
        pos=f[i]
        pos=pos.split(",")
        if eval(pos[1]) < one_less:
            empt=empt + pos[0]
            
    print("List of students who need to see an advisor:\n",empt,sep="")

    
student_analysis(f1=input("Enter the marks filename:\n"))


