#Denisha_Ramaloo

inputfile = input("Enter the input filname:\n")
openfile = open(inputfile,"r")
outputfile = input("Enter the output filename:\n")
Outfile = open(outputfile,"w")
lineWidth = int(input("Enter the line width:\n"))

words=[]

for i in openfile:
    word=i
    words.append(word)
    

words2=[]
for j in words:
    if j =="\n":
        help = "\n\n"
    else:
        help = j
    words2.append(help)    

words3=[]
for k in words2:
    newline= k[:len(k)-1]
    words3.append(newline)      
       
TW=""    
for z in words3:
    if TW=="":
        TW = z
    else:
        TW=TW+" "+z 
        
wordSpace = TW.split(" ")


wordcount = 0
listTally=[]
for t in wordSpace:
    if t =="\n":
        t = "\n\n"
        list1=t
        listTally.append(list1)
        wordcount = 0
    else:
        wordcount=wordcount + len(t)
        if wordcount<=lineWidth:
            list1=t+" "
            listTally.append(list1)
            wordcount = wordcount+1
        else:
            list1="\n"+t+" "
            wordcount=len(t) + 1
            listTally.append(list1)
  
        
Outfile.writelines(listTally)        
openfile.close()
Outfile.close()