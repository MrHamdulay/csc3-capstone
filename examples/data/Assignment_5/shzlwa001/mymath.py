# Definitions of Useful Math Functions
# Written by Lwazi Shezi
# 14.04.2014


def get_integer(string_to_compute):  # Converting a string to an integer
   numbers=["0","1","2","3","4","5","6","7","8","9"]
   print('Enter',string_to_compute+':')
   string=input()   
   for i in range(0,len(string)):
                  
      if string[0] in numbers:
            
            integer=eval(string)
            break
      else: 
         print('Enter',string_to_compute+':')
         string=input()           
         continue
   return integer 

def calc_factorial(number):  # Calculating a factorial of a number
   
   factorial=1
   for i in range(1,number+1):
      factorial=factorial*i
   return factorial


if __name__ == "__main__":
   main()
   
