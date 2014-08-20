h = eval(input("Enter the height of the triangle:\n"))
i = 0
line='*'
space=""
fullline=''

   

while i<h :
   fullline=''
   space=''
   for j in range(0, (h-i)) :
     
      space=space+" "
   fullline=space+line
   print(fullline)
   line=line+"**"
    
    
   i=i+1