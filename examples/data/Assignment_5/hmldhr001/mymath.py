#Dhriven Hamlall

def get_integer(a):
    num = (input ("Enter "+a+":\n"))
    while not num.isdigit ():
        num = (input ("Enter "+a+":\n"))#testing for letters and 0r negative digits
    num=eval(num) # eval makes it a digit practically 
    return num

def calc_factorial(a):
    answer = 1
    for i in range (a,1,-1):
        answer= answer * i
    return answer