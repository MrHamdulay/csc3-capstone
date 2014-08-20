def tree():
 for i in range(h):               
  print(seperator*gap+(tree_comp*s)+" "*gap) 
 gap-=1
 s+=2
 h=eval(input("Enter the height of the triangle:\n"))
 seperator=eval(input("Enter your seperator:"))
 x=h-1
 gap=x
 s=1
 tree_comp=input("Plugin in your tree component")

6
