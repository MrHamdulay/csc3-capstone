#Question 2


inputname=input("Enter the input filename:\n")
outputname=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

f=open(inputname,"r")
f1=f.read()

numlines=int(len(f1)/width)
print(numlines)

f2=""
k=40
for i in range(numlines):
   l=len(f1[(i-1)*width+k+1:(i-1)*width+40])
   f2=f2+f1[(i-1)*width+k+1:(i-1)*width+40]
   k=width-l
   while f1[i*width+k]!=" ":
      k=k-1
    #  print(k)
      #print(i)
   for j in range(k):
      f2=f2+f1[i*width+j]    
   f2=f2+"\n"
    
f2=f2+f1[(i)*width+k+1:(i)*width+40]
f2=f2+f1[(i+1)*width:]    

f.close()

f3=open(outputname,"w")
print(f2,file=f3)
f3.close()

