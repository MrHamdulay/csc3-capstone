"""Rishen Singh
Assignment 9 question 2
SNGRIS012"""
filename = input("Enter the input filename:\n")
f = open(filename,"r") #opens file
output = input("Enter the output filename:\n")
k = open(output,"w") #writes to new file
text=f.read() #stores the original file into list
position=0
count=-1
width = eval(input("Enter the line width:\n"))
i=0

while (i<len(text)): #runs through each item in the new list
    if(i==len(text)-1):
            new=[]
            new.append(text[count+1])
            
            for h in range(count+2,i):
                if(text[h]!='\n'): #adds to list while item is not a new line
                    new.append(text[h])
                else:
                    new.append(" ")
            new.append(text[i])      
            for h in new:
                print(h,end='',file=k)
                
    elif(text[i]=="\n" and text[i+1]=="\n"): #checks for when it moves to a new line
        new=[]
        new.append(text[count+1])
        for j in range(count+2,i):
            if(text[j]!='\n'):
                new.append(text[j]) #adds word to list while not a new line
            else:
                new.append(" ") #adds space if it is moving to a new line.
        new.append(text[i])
        for j in new:
            print(j,end='',file=k)
        print("",file=k)        
        
        count=i+1     
    
    elif(i==count+width and text[i+1]==" "): 
        new=[]
        new.append(text[count+1])
        for j in range(count+2,i):
            if(text[j]!='\n'):
                new.append(text[j])
            else:
                new.append(" ")
        new.append(text[i])
        for j in new:
            print(j,end='',file=k)
        print("",file=k)        
        
        count=i+1
    
    elif(i==count+width and text[i+1]!=" "):       
        for j in range(i,count,-1):
            if(text[j]==" " or text[j]=="\n"):
                position=j #sets position value to where there is a space or new line
                break
        new=[]
        new.append(text[count+1])
        for z in range(count+2,position-1): #runs through and prints according to column with and position to avoid any words being truncated
            if(text[z]!='\n'):
                new.append(text[z])
            else:
                new.append(" ")
        new.append(text[position-1])        
        for j in new:
            print(j,end='',file=k)
        print("",file=k)
        count=position
    i+=1

f.close()
k.close()