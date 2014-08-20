"""Program to reformat a textfile
Micaela Narasmulu
17 May 2014"""

filename = input("Enter the input filename:\n")

f = open(filename,"r") #open textfile 

output = input("Enter the output filename:\n")

k = open(output,"w")

txt=f.read() #puts textfile into a string

posit=0
count=-1
width = eval(input("Enter the line width:\n"))

for i in range(len(txt)):
    if(i==len(txt)-1):
            x=[]
            x.append(txt[count+1])
            for j in range(count+2,i):
                if(txt[j]!='\n'):
                    x.append(txt[j])
                else:
                    x.append(" ")
            x.append(txt[i])      
            for j in x:
                print(j,end='',file=k)
                
    elif(txt[i]=="\n" and txt[i+1]=="\n"):
        x=[]
        x.append(txt[count+1])
        for j in range(count+2,i):
            if(txt[j]!='\n'):
                x.append(txt[j])
            else:
                x.append(" ")
        x.append(txt[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        count=i+1     
    
    elif(i==count+width and txt[i+1]==" "):
        x=[]
        x.append(txt[count+1])
        for j in range(count+2,i):
            if(txt[j]!='\n'):
                x.append(txt[j])
            else:
                x.append(" ")
        x.append(txt[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        count=i+1
    
    elif(i==count+width and txt[i+1]!=" "):       
        for j in range(i,count,-1):
            if(txt[j]==" " or txt[j]=="\n"):
                posit=j
                break
            
        x=[] 
        x.append(txt[count+1])
        for j in range(count+2,posit-1):
            if(txt[j]!='\n'):
                x.append(txt[j])
            else:
                x.append(" ")
        x.append(txt[posit-1])        
        for j in x:
            print(j,end='',file=k)
        print("",file=k)
        count=posit

f.close()
k.close()