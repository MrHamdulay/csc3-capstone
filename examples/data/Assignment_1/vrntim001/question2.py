# TIM MOSTERT
# CSC1015F ASSIGNMENT 2: Q2

hour = eval(input("Enter the hours:\n"))
minute = eval(input("Enter the minutes:\n"))
second = eval(input("Enter the seconds:\n"))

if 0<=hour<=23 and 0<=minute<=59 and 0<=second<=59:
    print("Your time is valid.")
elif hour<0 or hour>23 or minute<0 or minute>59 or second<0 or second>59:
    print("Your time is invalid.")