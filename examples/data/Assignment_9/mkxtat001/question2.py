#prompt user for input
infile= input("Enter the input filename:\n")
outfile= input("Enter the output filename:\n")
width= int(input("Enter the line width:\n"))

f=open(infile,"r")
words=f.read() #store entire file in a single string
words = words.replace("\n\n"," 222 ")#replace the new line characters with a distinguishing character

list_lines=words.split("\n")
i = 0
while i < len(list_lines):
    if '' in list_lines:
        if list_lines[i]=='':
            list_lines[i-1]=list_lines[i-1]+"\n\n"
    i+=1 
    
string=" ".join(list_lines)
list_words = string.split(" ")    

f.close()
fout=open(outfile,"w")#open new file to write to

chrs=0
for word in list_words:
    if word=="222":
        print(file=fout)
        print(file=fout)
        chrs=0
        continue
    chrs+=len(word)+1  
    if chrs > width:
        print(file=fout)
        chrs=len(word)
      
    print(word,end=" ",file=fout)
print(file=fout)
print(file=fout)    
fout.close()