start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1,end):
  for x in range(2,i):
      if i%x == 0:
        break
      
  else:
    if(i>1):
      i=str(i)
      i_2=i[::-1]
      if i_2==i:
        
        print(i_2)
      
        
        


