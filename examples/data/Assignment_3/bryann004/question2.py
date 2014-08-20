he=int(input("Enter the height of the triangle:\n"))
sp=he-1
st=1

for i in range(he):
   print(" "*sp,"*"*st,sep="")
   st+=2
   sp-=1

