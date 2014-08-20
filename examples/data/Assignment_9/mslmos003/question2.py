getfile = input("Enter the input filname:\n")
openfile = open(getfile,"r")
outputfile = input("Enter the output filename:\n")
Outfile = open(outputfile,"w")
Width = int(input("Enter the line width:\n"))

words=[]

for i in openfile:
    word=i
    words.append(word)
    
               
words_2=[]
for x in words:
    if x =="\n":
        help = "\n\n"
    else:
        help = x
    words_2.append(help)     #words_2 = replaces the lines with "\n" with "\n\n"


words_3=[]
for y in words_2:
    newline= y[:len(y)-1]
    words_3.append(newline)   
   
       
G=""    #G will make it appear on a single line
for z in words_3:
    if G=="":
        G = z
    else:
        G=G+" "+z 
        
Space = G.split(" ") #prints

wordcount = 0
Tally=[]
for m in Space:
    if m =="\n":
        m = "\n\n"
        list1=m
        Tally.append(list1)
        wordcount = 0
    else:
        wordcount=wordcount + len(m)
        if wordcount<=Width:
            list1=m+" "
            Tally.append(list1)
            wordcount = wordcount+1
        else:
            list1="\n"+m+" "
            wordcount=len(m) + 1
            Tally.append(list1)
  
        
Outfile.writelines(Tally)        
openfile.close()
Outfile.close()