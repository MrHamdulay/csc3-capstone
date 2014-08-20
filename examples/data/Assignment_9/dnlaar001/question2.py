'''Question2 
Aaron Daniels
14 May 2014'''

name=input('Enter the input filename:\n')
f=open(name,'r')
text=f.read()
f.close()
outname=input('Enter the output filename:\n')
w=eval(input('Enter the line width:\n'))

p=0
for k in range(len(text)):
    if text[k]=='\n' and text[k-1]==' ':
        text=text[:k]+text[k+1:]+'*'
        p+=1
    elif text[k]=='\n' and text[k-1]=='-':
        text=text[:k]+text[k+1:]+'*'
        p+=1
    elif text[k]=='\n':
        text=text[:k]+' '+text[k+1:]

text=text[:len(text)-p]
y=text.split(' ')

fin=''
k=0
for c in range(len(y)):
    if k+len(y[c])+1<w:
        fin+=y[c]+' '
        k+=len(y[c])+1
    elif k+len(y[c])+1>w:
        fin+='\n'+y[c]+' '
        k=len(y[c])+1
    elif k+len(y[c])+1==w:
        fin+=y[c]+' '
        k+=len(y[c])+1
fin=fin[:len(fin)-2]
o=open(outname,'w')
print(fin,file=o)
o.close()
