m=input(("Enter the message:\n"))
mr=eval(input("Enter the message repeat count:\n"))
ft=eval(input("Enter the frame thickness:\n"))
l=0
ft2=ft
l2=ft
d=0

while ft>0:
    print("|"*l+"+"+("-"*len(m))+"-"*((ft-1)*2+2)+"+"+"|"*l)
    ft=ft-1
    l=l+1

while mr>0:
    print("|"*(ft2)+" "+m+" "+"|"*(ft2))
    mr=mr-1

while ft2 > 0:
    print((l2-1)*"|"+"+"+(len(m)*"-")+"-"*(d+2)+"+"+(l2-1)*"|")
    d=d+2
    ft2=ft2-1
    l2=l2-1