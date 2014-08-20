"""question 3 - Assignment 5
FRNHAN004
16 April 2014"""

#rewrite combine.py in a clear way with functions
global n, k, x, z #The purpose of the global statement is to declare that a function or method intends to change the value of a name from the global scope, that is, a name from outside the function.

#promps user to enter the integers to be used
def get_integern():
    global n
    n = input ("Enter n:\n")
    while not n.isdigit ():
        n = input ("Enter n:\n")
    n = eval (n)   
    
def get_integernk():
    global k 
    k = input ("Enter k:\n")
    while not k.isdigit ():
        k = input ("Enter k:\n")
    k = eval (k)    

def calc_factorialn(n):
    global nfactorial
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i    

def calc_factorialnk(y):
    global nkfactorial
    nkfactorial = 1
    for i in range (1, n-k+1):
        nkfactorial *= i    

get_integern()
get_integernk()
y=n-k
calc_factorialn(n)
calc_factorialnk(y)
print("Number of permutations:", nfactorial // nkfactorial)