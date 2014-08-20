import textwrap
plz=''
input1=input('Enter the input filename:\n')
f=open(input1,'r')
lines=f.readlines()
f.close
output=input('Enter the output filename:\n')
for i in lines:
 plz+=i
width = eval(input('Enter the line width:\n'))

work=''
x=textwrap.wrap(plz, width)


o=open(output,'w') 
for i in x:
 print(i,file=o)
o.close()

#output=input('Enter the output file name')
#f1=open(output,'w')
#for i in lines:
 #print(



