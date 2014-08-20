'''Joshen Credelio Jacob
14/05/2014'''


x=input('Enter the input filename:\n')
#y=input('Enter the output filename:\n')
#z=eval(input('Enter the line width:\n'))

f=open(x,'r')
l=f.readlines()
f.close()
list1=[]

#removing the carriage character
for i in l:
    if i[-1]=='\n':
        i = i[:-1]
        list1.append(i)

for i in range(len(list1)):
    print (list1[i])
    
