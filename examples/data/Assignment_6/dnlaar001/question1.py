t=[]
y=input('Enter strings (end with DONE):\n')
if y!='DONE':
    while y!='DONE':
        t.append(y)
        y=input('')
    x=t[0]
    for i in range(len(t)):
        mn=t[i]
        if len(mn)>len(x):
            x=mn
        else:
            ()
    print()
    print('Right-aligned list:')
    for i in range(len(t)):
        k=len(x)
        b='{0:>'+str(k)+'}'
        r=b.format(t[i])
        print(r)
elif y=='DONE':
    print()
    print('Right-aligned list:')
