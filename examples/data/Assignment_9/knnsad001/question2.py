#program to reformat a text file so that all lines are at most a given length
#KNNSAD001
#Assignment 9


filename = input("Enter the input filename:\n")
f = open(filename,"r")
output = input("Enter the output filename:\n")
s = open(output,"w")
first_text=f.read()
pos=[]

line_count=0
for i in range(len(first_text)): 
    if(i<len(first_text)-1 and first_text[i]==first_text[i+1]=="\n"):
        pos.append(i)
    
second_text=first_text.split("\n")
t_text=""
position=-1
for i in range(len(second_text)):
    t_text+=second_text[i]      
    
    if(i<len(second_text)-1):
        t_text=t_text+" "
        
print(len(t_text),len(first_text))
width=eval(input("Enter the line width:\n"))
count=-1
position=0

for i in range(len(t_text)):
    
    if(i==count+width and (t_text[i+1]==' ' or t_text[i+1]=='\n' or (t_text[i+1]!='\n' and t_text[i]=='\n') or (t_text[i+1]!=' ' and t_text[i]==' '))):
        if(t_text[count+1]==' '):
            print(t_text[count+2:i+1],file=s)
            
        else:
            print(t_text[count+1:i+1], file=s)
        count=i
        
    elif(i==count+width and t_text[i+1]!=' ' and t_text[i+1]!='\n'):
        
        for j in range(i,count,-1):
            if(t_text[j]==' '):
                position_=j
                break
            
        if(t_text[count+1]==' '):
            print(t_text[count+2:position_+1],file=s)
        else:
            print(t_text[count+1:position_+1],file=s)
        count=position_
        
    elif(i==len(t_text)-1):
        print(t_text[count+1:i+1],file=s)
        
    for j in range(len(pos)):
        if(i==pos[j]):
            print("",file=s)
            break
        
f.close()
s.close()