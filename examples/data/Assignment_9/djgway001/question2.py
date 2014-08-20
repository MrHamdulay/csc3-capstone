#printing paragraphs into equally lengthed lines
#wayne de jager
#13 may 2014

infile=input("Enter the input filename:\n") #the file from where info is obtained
outfile=input("Enter the output filename:\n") #the file being presented to
filein=open(infile, "r") #read the info
fileout=open(outfile, "w") #overwrite with the output
width=eval(input("Enter the line width:\n"))
string=filein.read()
x=string.splitlines(True) #splits with "\n"
string="".join(x)

parag=string.split("\n\n")
for i in range(len(parag)):
    parag[i] = parag[i].replace("\n", " ")

formatpara=[]
for para in parag:
    para=para.split(" ") #spliting on the space character
    newstr=[]
    count=0
    for i in para:
        if count+int(len(i))<=width:   
            newstr.append(i) #appending to newstring grid
            newstr.append(" ")
            count=count+int(len(i)+1)
        else:
            newstr.append("\n")  
            count=0
            newstr.append(i)
            newstr.append(" ")
            count=count+int(len(i)+1)
    formatpara.append(newstr)

for i in formatpara:
    if i[-1]==" ":
        i[-1]=""
    else: continue

for para in formatpara:
    string="".join(para)
    string=string+"\n"
    print(string, file=fileout)
  
filein.close()
fileout.close()