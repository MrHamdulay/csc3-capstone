def print_square():
 for i in range(6):
  if i == 0 or i== 5:
   print("*****")
  elif 1<i<5: 
   print("*"+"   "+"*")

def print_rectangle(width,height):
  for i in range(height):
   if i==0 or i==height-1:
    print("*"*width)
   elif i!=0 or i!= height:
    print("*"+(width-2)*" " +"*")

def get_rectangle(width, height):
 x =(width*"*" +" \n")
 a = 0
 z = ("*"+(width-2)*" " +"* \n")
 while a < height:
  if a==1 or a==height-1:
   y = x 
  else:
   y = z
   b=y*(height-2)
  a+=1
 return (y+b+y)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#def get_rectangle():