

def square(a):
      for i in range(a):
            if i>0 and i<a-1:
                  print('*'+' '*(a-2)+'*')        
            else:
                  print('*'*a)    

def rectangle(a,c):
      for i in range(a):
            if i>0 and i<a-1:
                  print('*'+' '*(c-2)+'*')        
            else:
                  print('*'*c)

if __name__=="__main__":
      square(5)


