'''Question2 -Assignment 9- wrapping text
GVNPRI022-Prinesan Govender
13 May 2014'''
import textwrap
filename= input("Enter the input filename:\n")

f= open(filename,"r") #reading in file
listData= f.readlines()
f.close()
out_filename=input("Enter the output filename:\n")
widthLine= eval(input("Enter the line width:\n"))
newListData=[]           
oneline=""

for i in range(len(listData)):
    length= len(listData[i])
    if listData[i]== '\n':
        listData[i]= "###" #replacing line with ### to denote end of paragraph
     
         
            
                        
for i in range (len(listData)):
    
    
        
        oneline=oneline+""+listData[i]+"" #concatenating string
 

paragraph= oneline.split("###") #splitting paragraphs
for i in range (len(paragraph)):
    
    newListData.append(textwrap.wrap(paragraph[i],width=widthLine)) #using textwrap module to wrap text


newF2= open(out_filename,"w") #writing to ouput textfile
for j in range(len(newListData)):
    
    for i in range(len(newListData[j])):
        print(newListData[j][i],file=newF2)
    
    print(file=newF2)
    

newF2.close()