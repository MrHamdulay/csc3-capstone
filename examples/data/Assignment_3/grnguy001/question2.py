a=eval(input("Enter the height of the triangle:\n"))
b=a-1 
for i in range(0,2*a,2):
          print(' '*b, "*"*(i+1), sep="") 
          b=b-1 