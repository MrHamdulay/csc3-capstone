
original=input("Enter the input filename:\n")
file1=open(original,'r')
contents=file1.read()
file1.close()
words=contents.split(' ')
alternate=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
file2=open(alternate,'w')
length=0
for i in range(len(words)):
    length+=len(words[i])
line=0
for a in range(len(words)):
    if a==len(words)-1 and (line+len(words[a]))<=width:
        add=words[a]
        file2.write(add)
    elif a==len(words)-1 and (line+len(words[a]))>width:
        add=words[a]
        file2.write('\n')
        file2.write(add)
    elif (line+len(words[a]))<width:
        add=words[a]+' '
        file2.write(add)
        line+=len(add)
    elif (line+len(words[a]))==width:
        add=words[a]
        file2.write(add)
        line+=len(add)
    else:
        add=words[a]+' '
        file2.write('\n')
        file2.write(add)
        line=0
        line+=len(add)
file2.close()