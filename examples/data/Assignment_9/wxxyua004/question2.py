"""program to reformat text and put into another folder
yuan-yow wu
16 may 2014"""

inputfile = input("Enter the input filname:\n")
openfile = open(inputfile,"r")
outputfile = input("Enter the output filename:\n")
Outfile = open(outputfile,"w")
lineWidth = int(input("Enter the line width:\n"))

words=[]

for i in openfile:
    word=i
    words.append(word)
    
#print(words)               #words = each line split ending in \n
words2=[]
for j in words:
    if j =="\n":
        help = "\n\n"
    else:
        help = j
    words2.append(help)     #words2 = replace lines with only "\n" with "\n\n"
#print(words2)

words3=[]
for k in words2:
    newline= k[:len(k)-1]
    words3.append(newline)   #words3 = minus the "\n" (only 1)
#print(words3)    
       
TW=""    
for z in words3:
    if TW=="":
        TW = z
    else:
        TW=TW+" "+z #TW makes it all one long line
#print(TW)        
wordSpace = TW.split(" ")
#print(wordSpace)

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