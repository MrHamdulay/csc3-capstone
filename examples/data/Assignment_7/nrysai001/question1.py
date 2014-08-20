print('Enter strings (end with DONE):')
a=[]
x = ""
while x!='DONE':
    x=input()
    if x=='DONE':
        break
    if x not in a:
        a.append(x)
print()
print("Unique list:")
for i in range(len(a)):
    print(a[i])
 
 

