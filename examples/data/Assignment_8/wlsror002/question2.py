#function to count pairs of repeated letters
def count(x,y):
   if x=='' or len(x)==1:
      return y
   elif x[0]==x[1]:
      return count(x[2:],y+1)
   else: 
      return count(x[2:],y)
      
   
def main():
   y=0
   x=input('Enter a message:\n')
   Count=count(x,y) 
   print ('Number of pairs:',Count)
    
main()