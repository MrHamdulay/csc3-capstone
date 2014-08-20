#Rushil Kalidas
#19 May 2014

inputfile = input("Enter the input filname:\n")
openfile = open(inputfile,"r") #Opening the file

outputfile = input("Enter the output filename:\n")
outfile = open(outputfile,"w")

linewidth = int(input("Enter the line width:\n"))

words=[]

for i in openfile:
    word=i
    words.append(word)
    

w2=[]
for j in words:
    if j =="\n":
        help = "\n\n"
    else:
        help = j
    w2.append(help)     

w3=[]
for k in w2:
    newline= k[:len(k)-1]
    w3.append(newline)   


r=""    
for z in w3:
    if r=="":
        r = z
    else:
        r=r+" "+z 
        
wordSpace = r.split(" ")

wordcount = 0
listCount=[]

for t in wordSpace:
    
    if t =="\n":
        t = "\n\n"
        list1=t
        listCount.append(list1)
        wordcount = 0
        
    else:
        wordcount=wordcount + len(t)
        if wordcount<=linewidth:
            list1=t+" "
            listCount.append(list1)
            wordcount = wordcount+1
            
        else:
            list1="\n"+t+" "
            wordcount=len(t) + 1
            listCount.append(list1)
  
        
outfile.writelines(listCount)        
outfile.close()
openfile.close() #Closing files
