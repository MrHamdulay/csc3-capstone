#Program to reformat a textfile
#romelon chetty
#16 May 2014

filename = input("Enter the input filename:\n") # get input text file 
opin = open(filename,"r")
output = input("Enter the output filename:\n") # get output text file
opout= open(output,"w")
text=opin.read() # read text into one string
posit=0
count=-1
width = eval(input("Enter the line width:\n")) # specified width from user
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
                print(j,end='',file=opout)
                
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
            print(j,end='',file=opout)
        print("",file=opout)        
        
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
            print(j,end='',file=opout)
        print("",file=opout)        
        
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
            print(j,end='',file=opout)
        print("",file=opout)
        count=posit

opin.close()
opout.close()