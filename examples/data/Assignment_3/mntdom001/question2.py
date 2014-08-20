# question2.py
# Author: Dominic Manthoko
# 22 March 2014

def tri(c_height, gap, symbol):
   for i in range(0,c_height,2):
      print(' '*gap,end='')  
      print(symbol*(i+1))
      gap -= 1
        
if __name__ == '__main__':
   # ask the user to input a height and convert to a new value
   # call the converted height c_height
   height = eval(input("Enter the height of the triangle: \n"))
   c_height = (2 * height) - 1  
      
   gap= c_height//2 
   symbol = '*'
   
   tri(c_height, gap, symbol)
