alligned_list=[]
x=0
x=input('Enter strings (end with DONE):\n')
alligned_list.append(x)
while x!='DONE':
    x=input()
    alligned_list.append(x)
print()
print('Right-aligned list:')
alligned_list.remove(alligned_list[-1])
gap=' '
y=0
for i in alligned_list:
    if len(i)>y:
        y=len(i)
for j in alligned_list:
    print((y-len(j))*gap,j,sep='')
    