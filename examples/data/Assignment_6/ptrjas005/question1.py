'''Jason Pietersen'''
x= input('Enter strings (end with DONE):\n')


y=[]
 
while (x!='DONE'):
  y.append(x)
  x= input()

  

#Right Align List
print()
print('Right-aligned list:')
for i in y:
  width= len(i)
  max_=0
  
  if (len(i)>max_):
    max_=i
  
form = '{0:>'+str(len(max_))+'}'
for name in y:
  print(form.format(name))

