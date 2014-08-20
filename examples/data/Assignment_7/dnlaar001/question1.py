q=input('Enter strings (end with DONE):\n')
w=[]
if q!='DONE':
    w.append(q)
while q!='DONE':
    if q in w:
        ()
    else:
        w.append(q)
    q=input()
print()
print('Unique list:')
for i in range(len(w)):
    print(w[i])
    