def get_integer(x):
   answer=input("Enter "+x+":\n")
   while not answer.isdigit ():
      answer=input("Enter "+x+":\n")
   answer = eval (answer)  
   return answer
    

def calc_factorial(x):
   factorial = 1
   for i in range (1, x+1):
      factorial *= i
   return factorial
   

    
        