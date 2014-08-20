def decimal_to_ndom (a):
   tot = ""
   while a: 
      y = a % 6
      a = a // 6
      tot = tot + str(y)
      
   fin = eval(tot[::-1]) 
   return (fin)  
 
   
def ndom_to_decimal(a):
   tot = 0
   l = len(str(a)) - 1
   for i in str(a):
      d = (i + l*"0")
      dd = eval(d[0:1])
      tot = tot + (dd*(6**l))
      l = l - 1
   return tot
   
   
def ndom_add(a,b):
   x = ndom_to_decimal(a) + ndom_to_decimal(b) 
   y = decimal_to_ndom (x)
   return y

def ndom_multiply(a,b):
   x = ndom_to_decimal(a) * ndom_to_decimal(b) 
   y = decimal_to_ndom (x)
   return y
