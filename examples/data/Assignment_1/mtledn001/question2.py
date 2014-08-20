#MTLEDN001 Sewagodimo Matlapeng
#Assignment 1 question 2
#Computer Sciences 1015F
# 25 February 2014
hour,minute,second = eval(input("Enter the hours:\n")),eval(input("Enter the minutes:\n")),eval(input("Enter the seconds:\n")) 
if(0<=hour<=23 and 0<=minute<=60 and 0<=second<=60):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
    
