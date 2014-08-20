""" Assignment 5 Questiosn 2 by Jonathan Ovadia
on the 16 April 2014"""

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    money = []
    while cost> sum(money):
        money.append(eval(input("Deposit a coin or note (in cents):\n")))
    change = sum(money) - cost
    print(calc_change(change))
def calc_change(c):
    s = ""
    one = c//100
    tf = (c-one*100)//25
    ten = (c-one*100-25*tf)//10
    five = (c-one*100-25*tf - ten*10)//5
    onec = (c-one*100-25*tf - ten*10-five*5)//1
    if one  > 0 or tf > 0 or ten > 0 or five > 0 or onec > 0:
        s = "Your change is:\n"
    if one != 0 :
        s += str(one) +" x $1\n"
    if tf != 0 :
        s += str(tf) +" x 25c\n"
    if ten != 0 :
        s += str(ten) +" x 10c\n"
    if five != 0 :
        s += str(five) +" x 5c\n"
    if onec != 0 :
        s += str(onec) +" x 1c\n"
    return s
    
    
main()