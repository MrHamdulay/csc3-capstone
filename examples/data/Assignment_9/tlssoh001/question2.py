'''Sohail Tulsi 
TLSSOH001
14/05/2014
Programme to reformat a text file so that all lines are at a given length'''
    
    #get user input
infile=input("Enter the input filename:\n")
outfile=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
    
    #read file contents
f=open(infile,"r")
text=f.readlines()
   
    
    #removes newline value
for i in range(len(text)-1):
    if text[i]==" ":
        continue
    else:
        text[i]=text[i][:len(text[i])-1]
    
    #joins list values into 1 string
textStr=" ".join(text) 
    #split line into words
words=textStr.split(" ")
x=words.count("")

    #adds words to a line if less than width
numlines= len(textStr)//width +2+x
lines=[""]*numlines   
pos=0
    
for i in range (len(lines)):
    line=""
    count=0
    while count<=width+1 and pos<len(words):
        count+=len(words[pos])+1
        if words[pos]=="":
            lines[i]=line
            count=width+1
            pos+=1
   
        elif count<=width+1:
            line=line+words[pos]+" "
            pos+=1
        else:
            #count-=len(words[pos])+1
            continue
            
    if lines[i] == "":
        lines[i]=line

    else:
        lines[i]=line+"\n"
        
    #prints lines
f2=open(outfile,"w")
for l in lines:
    print(l,file=f2)
    
f.close()    
f2.close()
