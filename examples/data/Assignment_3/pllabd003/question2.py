# question2
        
a= eval(input("Enter the height of the triangle:\n"))
number=1
gap=a-1 

for i in range(a):
          print(' '*gap, "*"*number, sep="")  
          number+=2
          gap=gap-1 # can also write this as: gap-=1
          