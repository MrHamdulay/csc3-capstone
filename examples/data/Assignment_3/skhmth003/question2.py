def stupid2():
      a=eval(input("Enter the height of the triangle:\n"))
      j=1
      i=a-1
      for b in range(a):
            print(" "*i,"*"*j,sep="")
            j+=2
            i-=1
stupid2()