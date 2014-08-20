import textwrap
i=input('Enter the input filename:\n')
inputfil=open(i,'r')
temp=inputfil.read()
words=temp.split('\n\n')
inputfil.close()
outfil=input('Enter the output filename:\n')
w=eval(input('Enter the line width:\n'))
new_file=open(outfil,'w')
for ln in words:
    ln=ln.replace('\n',' ')
    width=w
    ln=textwrap.wrap(ln,width)
    leng=len(ln)
    for letter in range(leng):
        print(ln[letter],file=new_file)
    print(file=new_file)
new_file.close()