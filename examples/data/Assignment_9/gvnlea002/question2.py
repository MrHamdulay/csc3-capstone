"""17 may 2014
leandra govender
program to reformat a text file so that all lines are at most a given length"""


filename = input("Enter the input filename:\n")
f = open(filename,"r")                  #open to read only
output = input("Enter the output filename:\n")
k = open(output,"w")                   #open to overwrite contents of the file
text=f.read()
posit=0
count=-1
width = eval(input("Enter the line width:\n"))         #ask for the given width
for i in range(len(text)):              #use a for loop with if elses to check if the lines a greater than , equal too or less than the given width
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
k.close()                        #close files