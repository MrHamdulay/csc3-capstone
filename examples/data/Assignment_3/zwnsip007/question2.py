height=eval(input("Enter the height of the triangle:"'\n'))
for i in range(1,2*height+1,2):
   q=("{:^"+str(2*height-1)+"}")
   print(q.format("*"*i))
   