#Michael_Odhiambo
#ODHMIC003
a= input("Enter the message:"'\n')
b= eval(input("Enter the message repeat count:"'\n'))
c= eval(input("Enter the frame thickness:"'\n'))
d= len(a)
e=d+2
i=e+2*(c-1)
j=0
p=c-1
o=e
u=c-1
t= (e-d)//2
while i >= e and j < c:
    print('|'*j+'+'+'-'*i+'+'+'|'*j)
    i=i-2
    j=j+1
for h in range(b):
    print('|'*c+' '*t+a+' '*t+'|'*c)
while e+2*c>o>=e:
    print('|'*u+'+'+'-'*o+'+'+'|'*u)
    p=p-1
    o=o+2
    u=u-1