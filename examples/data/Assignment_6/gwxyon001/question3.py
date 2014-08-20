#elections
#YONGAMA GIWU
#21 april 2014
print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
A=[]
z='{0:<10}'
B=[]
while True:
    x=input('')
    if x=='DONE':
        break
    A.append(x)
print()
print('Vote counts:')
A.sort()
acc=0
for i in range(len(A)):
    
    if len(A)==1:
        i=0
        a=A[0]
        print(z.format(a),' - ',1,sep='')
        A.remove(a)
        break
    if len(A)==0:
            break    
    a=A[0]
    count=A.count(a)
    if count>=1:
        for i in range(count):
            A.remove(a)
        acc+=1
        print(z.format(a),' - ',count,sep='')
        
   # elif count==1:
    #    for i in range(count):
     #       A.remove(a)
     #   acc+=1
      #  print(z.format(a),' - ',count,sep='')
        
        
        