filename = input("Enter the input filename:\n")
f = open(filename,"r")
output = input("Enter the output filename:\n")
k = open(output,"w")
text=f.read()
posit=0
count=-1
width = eval(input("Enter the line width:\n"))
for i in range(len(text)):
    if(i==len(text)-1):
            x=[]
            x.append(text[count+1])
            for j in range(count+2,i):
                if(text[j]!='\n'):
                    x.append(text[j])
                else:
                    x.append(" ")
            x.append(text[i])      
            for j in x:
                print(j,end='',file=k)
                
    elif(text[i]=="\n" and text[i+1]=="\n"):
        x=[]
        x.append(text[count+1])
        for j in range(count+2,i):
            if(text[j]!='\n'):
                x.append(text[j])
            else:
                x.append(" ")
        x.append(text[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        count=i+1     
    
    elif(i==count+width and text[i+1]==" "):
        x=[]
        x.append(text[count+1])
        for j in range(count+2,i):
            if(text[j]!='\n'):
                x.append(text[j])
            else:
                x.append(" ")
        x.append(text[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        count=i+1
    
    elif(i==count+width and text[i+1]!=" "):       
        for j in range(i,count,-1):
            if(text[j]==" " or text[j]=="\n"):
                posit=j
                break
        x=[]
        x.append(text[count+1])
        for j in range(count+2,posit-1):
            if(text[j]!='\n'):
                x.append(text[j])
            else:
                x.append(" ")
        x.append(text[posit-1])        
        for j in x:
            print(j,end='',file=k)
        print("",file=k)
        count=posit

f.close()
k.close()