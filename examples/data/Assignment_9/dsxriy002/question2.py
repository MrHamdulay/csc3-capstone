#Riya Desai
#Assignment 9 - Question 2
#14 May 2014


#ask user to choose a file
nameoffile = input("Enter the input filename:\n")



f = open(nameoffile,"r")
output = input("Enter the output filename:\n")

#allow file lines to be edited(overwrite)
x = open(output,"w")

text1=x.read()

position=[]

count_lines=0

for i in range(len(text1)): 
    if(i<len(text1)-1 and text1[i]==text1[i+1]=="\n"):
        position.append(i)
    
secondtext=text1.split("\n")

text=""
position=-1

for i in range(len(secondtext)):
    text+=secondtext[i]       
    
    if(i<len(secondtext)-1):
        text=text+" "
print(len(text),len(text1))


#ask user for the width of the line
linewidth=eval(input("Enter the line width:\n"))
count=-1


position_next=0

for i in range(len(text)):
    
    if(i==count+linewidth and (text[i+1]==' ' or text[i+1]=='\n' or (text[i+1]!='\n' and text[i]=='\n') or (text[i+1]!=' ' and text[i]==' '))):
        
        if(text[count+1]==' '):
            print(text[count+2:i+1],file=y)
       
        else:
            print(text[count+1:i+1], file=y)
        count=i
    
    
    elif(i==count+linewidth and text[i+1]!=' ' and text[i+1]!='\n'):       
        for j in range(i,count,-1):
            if(text[j]==' '):
                position_next=j
                break
        
        
        if(text[count+1]==' '):
            print(text[count+2:position_next+1],file=y)
        
        else:
            print(text[count+1:position_next+1],file=y)
        count=position_next
    
    
    elif(i==len(text)-1):
        print(text[count+1:i+1],file=y)
    
    for j in range(len(position)):
        if(i==position[j]):
            print("",file=y)
            break    

#close both files
f.close()
y.close()