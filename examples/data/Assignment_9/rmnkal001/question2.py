#Kalind Ramnarayan
#text allignment
#11 May 2014


filename = input("Enter the input filename:\n")     #open file
f = open(filename,"r")
output = input("Enter the output filename:\n")
k = open(output,"w")
text1=f.read()
pos=[]


for i in range(len(text1)): 
    if(i<len(text1)-1 and text1[i]==text1[i+1]=="\n"):
        pos.append(i)
    
text2=text1.split("\n")                           #create a list of lines
text=""
position=-1
for i in range(len(text2)):
    text+=text2[i]       
    if(i<len(text2)-1):
        text=text+" "
print(len(text),len(text1))
width=eval(input("Enter the line width:\n"))
count=-1
posit=0

for i in range(len(text)):  # slicing the text in order to allign
    
    if(i==count+width and (text[i+1]==' ' or text[i+1]=='\n' or (text[i+1]!='\n' and text[i]=='\n') or (text[i+1]!=' ' and text[i]==' '))):
        if(text[count+1]==' '):
            print(text[count+2:i+1],file=k)
        else:
            print(text[count+1:i+1], file=k)
        count=i
    elif(i==count+width and text[i+1]!=' ' and text[i+1]!='\n'):       
        for j in range(i,count,-1):
            if(text[j]==' '):
                posit=j
                break
        if(text[count+1]==' '):
            print(text[count+2:posit+1],file=k)
        else:
            print(text[count+1:posit+1],file=k)
        count=posit
    elif(i==len(text)-1):
        print(text[count+1:i+1],file=k)
    for j in range(len(pos)):
        if(i==pos[j]):
            print("",file=k)
            break    
f.close()
k.close()