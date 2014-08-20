print('Independent Electoral Commission')
print('--------------------------------')
q=input('Enter the names of parties (terminated by DONE):\n')
w=[]
e=[]
if q!='DONE':
    w.append(q)
while q!='DONE':
    if q in w:
        ()
    else:
        w.append(q)
    e.append(q)
    q=input()
w.sort()
print()
print('Vote counts:')
for r in range(len(w)):
    t=e.count(w[r])
    print(str(w[r]),end='')
    y=' - '+str(t)
    i=10+(10-len(w[r]))-6
    o='{0:>'+str(i)+'}'
    u=o.format(y)
    print(u)
