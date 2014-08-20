y=[]
b=input('Enter strings (end with DONE):\n')
while b!='DONE':
    y.append(b)
    b=input('')

if len(y) > 0:
    x=len(y[0])

for i in range (1,len(y),1):
    temp = len(y[i])
    if (temp > x):
        x = temp

print('\nRight-aligned list:')
for i in range(len(y)):
    print(" " * (x - len(y[i])) + y[i])
            
            