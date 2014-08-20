textin = input("Enter the input filename:\n")
textout = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open(str(textin))
text = f.read()
f.close()

word = text.split()

x = 0
wrd = 0

newf = open(str(textout),'w')
for j in range(len(word)):
    wrd += len(word[j])
    if wrd < width:
        print(word[j],end=' ',file=newf)
        x+=1
        wrd+=1
    else:
        print('\n',end='',file=newf)
        print(word[j],end=' ',file=newf)
        wrd = len(word[j])
newf.close()