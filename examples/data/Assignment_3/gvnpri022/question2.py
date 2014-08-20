
h= eval(input("Enter the height of the triangle:\n"))
cen=2*h-1
for i in range(1,h+1):
    s="*"*((2*i)-1)
   
    s=s.center((cen))
    print(s)
