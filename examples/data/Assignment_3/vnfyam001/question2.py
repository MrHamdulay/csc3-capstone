x=eval(input("Enter the height of the triangle:\n"))
t="*"
tr=1
for i in range(x):
 y=(x-1)-i
 print(" "*y,t*tr,sep="")
 tr=tr+2
