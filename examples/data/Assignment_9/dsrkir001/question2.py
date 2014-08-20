#Program to reformat a text file so that all lines are at most a given length
#13 May 2014
#Kiran Desraj

#get files

ifile = input("Enter the input filename:\n")

a = open(ifile,"r")

ofile = input("Enter the output filename:\n")

b = open(ofile,"w")

folder = a.read()

open=[]

count_lines=0

for i in range(len(folder)): 
    if(i<len(folder)-1 and folder[i]==folder[i+1]=="\n"):
        open.append(i)
    
folder_2 = folder.split("\n")

words = ""

position = -1

for i in range(len(folder_2)):
    words+=folder_2[i]       
    if(i<len(folder_2)-1):
        words += " "
print(len(words),len(folder))


number = (0-1)
line_width=eval(input("Enter the line width:\n"))

placeholder = 0




#justify text

for i in range(len(words)):
    
    if(i==number+line_width and (words[i+1]==' ' or words[i+1]=='\n' or (words[i+1]!='\n' and words[i]=='\n') or (words[i+1]!=' ' and words[i]==' '))):
        if(words[number+1]==' '):
            
            print(words[number+2:i+1],file=b)
            
        else:
            
            print(words[number+1:i+1], file=b)
        number=i
        
    elif(i==number+line_width and words[i+1]!=' ' and words[i+1]!='\n'):       
        for j in range(i,number,-1):
            if(words[j]==' '):
                placeholder=j
                break
            
        if(words[number+1]==' '):
            print(words[number+2:placeholder+1],file=b)
            
        else:
            
            print(words[number+1:placeholder+1],file=b)
        number=placeholder
    elif(i==len(words)-1):
        
        print(words[number+1:i+1],file=b)
    for j in range(len(open)):
        if(i==open[j]):
            print("",file=b)
            break 
        
    #close files
    
a.close()
b.close()