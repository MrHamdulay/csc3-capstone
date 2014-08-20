"""Question 2
Alexi Kalamoudacos
14 May 2014"""

x=input('Enter the input filename:\n')
y=input('Enter the output filename:\n')
z=eval(input('Enter the line width:\n'))
b=0
f=open(x,'r')
a = f.readlines()
f.close()
for i in range (len (a)-1):
    a[i] = a[i][:-1] #removing character
c=[]
for i in range(len(a)):
    if a[i]=='':
        c.append(['\n\n']) #checking text
    else:
        c.append(a[i].split(' '))
f=open(y, 'w')
for i in range(len(c)):
    for j in range(len(c[i])):
        if b==0:
            b=len(c[i][j])+1
            print(c[i][j],end=' ',file=f) #1st word in text
        elif c[i][j]=='\n\n':
            b=0
            print(c[i][j],sep='',end='',file=f) #inserting the paragraph empty line
        elif len(c[i][j])+b>z: #wrapping
            print('\n',c[i][j],sep='',end=' ',file=f)
            b=len(c[i][j])+1
        else:
            if len(c[i][j])+b<=z: 
                b+=len(c[i][j])+1         
                print(c[i][j],end=' ',file=f)
            else:
                print(c[i][j],end='',file=f)
f.close() 