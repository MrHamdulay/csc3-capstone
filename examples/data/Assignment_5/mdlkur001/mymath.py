#KURESHLEN MOODLEY
#14/04/14
#MDLKUR001
def get_integer(x):
    t = input ("Enter "+x+":\n")
    while not t.isdigit ():
        t =input ("Enter "+x+":\n")
    t= eval(t)
    return t

def calc_factorial(x):
    factorial = 1
    for i in range (1, x+1):
        factorial *= i
    return factorial