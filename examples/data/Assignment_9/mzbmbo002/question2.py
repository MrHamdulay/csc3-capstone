#Mbongeni Mazibuko
#MZBMBO002
#Assignment 9 Q2

file=input('Enter the input filename:\n')
newfile= input('Enter the output filename:\n')
width= eval(input('Enter the line width:\n'))
f= open(file,'r')
ltext= f.readlines()
text= ''.join(ltext)
#at this point textfile is a string
ltext= text.split('\n')
for i in range(len(ltext)):
    if ltext[i]=='':
        ltext[i]='\n\n'
        #find beginning of new paragraph
text= ' '.join(ltext)
#at this point textfile is a string with each word seperated by a space
ltext= text.split(' ')
#at this point every individual word is in an index
lnew=''
lwidth=width
f.close()

for i in range(len(ltext)):
    if lwidth-len(ltext[i])>=0:
        #appends a line of the new string as long as the width is >= to that of which the user entered
        if ltext[i]=='\n\n':
            #makes a paragragh where there were two new lines once existed
            lnew+=ltext[i]
            lwidth=width
            #width reseted
        else: 
            lnew+= ltext[i]+' '
            lwidth-=len(ltext[i])+1
            #width is minus the new word added plus space
    else:
        #new line is started
        lnew= lnew[:-1]+'\n'+ltext[i]+' '
        lwidth= width-(len(ltext[i])+1)

newf= open(newfile, 'w')
#new string is written in new file
print(lnew, file=newf)
newf.close()