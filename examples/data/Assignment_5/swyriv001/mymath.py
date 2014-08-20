"""program that has reused functions
  Rivoningo Seweya 
  10 April 2014"""
#function that obtains the n and k values
def get_integer (letter):
    if letter=="n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n) 
        return n
    if letter=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k) 
        return k
 #fuction that calculates the factorial       
def calc_factorial(n):
   # get_integer(letter)
        factorial = 1
        for i in range (1, n+1):
            factorial *= i   
        return (factorial)

    