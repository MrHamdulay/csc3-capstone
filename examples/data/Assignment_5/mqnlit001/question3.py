#Litha Maqungo
#16 April 2014
#Permutations-combining two existing functions

def get_integer(x): #this is the function that allows the user to enter their n and k
            if x == "n": #it will either be n or k hence the if statement
                        print("Enter n:")
                        n=(input)
                        while not n.isdigit ():
                                    n=input("Enter n: \n")
                        return eval(n)
            
            else: 
                        print("Enter k:")
                        k=int(input())
                        while not k.isdigit ():
                                    k=input("Enter k: \n")
                        return eval(k)
            
def calc_factorial (y): #this is the function that gets the factorials to use to determine permutations
            factorial = 1
            for i in range(1, y+1):
                        factorial *= i  
            return factorial 
         






   