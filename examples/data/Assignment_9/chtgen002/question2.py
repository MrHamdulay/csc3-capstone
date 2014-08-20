"""CHTGEN002
12/05/14
Reformatting
"""
filename = input("Enter the input filename:\n")
f = open(filename,"r")
output = input("Enter the output filename:\n")
k = open(output,"w")
oldtxt=f.read()
posit=0
num=-1
limit = eval(input("Enter the line limit:\n"))

for i in range(len(oldtxt)):
    if(i==len(oldtxt)-1):
            x=[]
            x.append(oldtxt[num+1])
            for j in range(num+2,i):
                if(oldtxt[j]!='\n'):
                    x.append(oldtxt[j])
                else:
                    x.append(" ")
            x.append(oldtxt[i])      
            for j in x:
                print(j,end='',file=k)
                
    elif(oldtxt[i+1]=="\n" and oldtxt[i]=="\n"):
        x=[]
        x.append(oldtxt[num+1])
        for j in range(num+2,i):
            if(oldtxt[j]!='\n'):
                x.append(oldtxt[j])
            else:
                x.append(" ")
        x.append(oldtxt[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        num=i+1     
    
    elif(oldtxt[i+1]==" " and i==num+limit):
        x=[]
        x.append(oldtxt[num+1])
        for j in range(num+2,i):
            if(oldtxt[j]!='\n'):
                x.append(oldtxt[j])
            else:
                x.append(" ")
        x.append(oldtxt[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        num=i+1
    
    elif(oldtxt[i+1]!=" " and i==num+limit):       
        for j in range(i,num,-1):
            if(oldtxt[j]==" " or oldtxt[j]=="\n"):
                posit=j
                break
        x=[]
        x.append(oldtxt[num+1])
        for j in range(num+2,posit-1):
            if(oldtxt[j]!='\n'):
                x.append(oldtxt[j])
            else:
                x.append(" ")
        x.append(oldtxt[posit-1])        
        for j in x:
            print(j,end='',file=k)
        print("",file=k)
        num=posit

f.close()
k.close()