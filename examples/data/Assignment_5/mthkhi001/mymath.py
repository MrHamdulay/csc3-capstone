#Khiraad Mathura
#MTHKHI001
#Question3

def get_integer(a):
    integer = -1
    stringtest = False
    while integer == -1 and stringtest == False:
        try:
            integer = int(input("Enter " + a +":\n"))
        except ValueError:
            continue
        
        if integer == -1:
            continue
        
        else:
            return integer
        break
    

def calc_factorial(b):
    factorial = 1
    for i in range(1, b+1):
        factorial *= i
    return factorial
