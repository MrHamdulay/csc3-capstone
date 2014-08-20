#NDXMIC014
#ASSIGNMENT 9
#QUESTION 2

file_name = input("Enter the input filename:\n")
f = open(file_name,"r")
output = input("Enter the output filename:\n")
k = open(output,"w")
txt=f.read()
position=0
counter=-1
width = eval(input("Enter the line width:\n"))
for i in range(len(txt)):
    if(i==len(txt)-1):
            x=[]
            x.append(txt[counter+1])
            for j in range(counter+2,i):
                if(txt[j]!='\n'):
                    x.append(txt[j])
                else:
                    x.append(" ")
            x.append(txt[i])      
            for j in x:
                print(j,end='',file=k)
                
    elif(txt[i]=="\n" and txt[i+1]=="\n"):
        x=[]
        x.append(txt[counter+1])
        for j in range(counter+2,i):
            if(txt[j]!='\n'):
                x.append(txt[j])
            else:
                x.append(" ")
        x.append(txt[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        counter=i+1     
    
    elif(i==counter+width and txt[i+1]==" "):
        x=[]
        x.append(txt[counter+1])
        for j in range(counter+2,i):
            if(txt[j]!='\n'):
                x.append(txt[j])
            else:
                x.append(" ")
        x.append(txt[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        counter=i+1
    
    elif(i==counter+width and txt[i+1]!=" "):       
        for j in range(i,counter,-1):
            if(txt[j]==" " or txt[j]=="\n"):
                position=j
                break
        x=[]
        x.append(txt[counter+1])
        for j in range(counter+2,position-1):
            if(txt[j]!='\n'):
                x.append(txt[j])
            else:
                x.append(" ")
        x.append(txt[position-1])        
        for j in x:
            print(j,end='',file=k)
        print("",file=k)
        counter=position

f.close()
k.close()