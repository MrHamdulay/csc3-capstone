#Program to test valid time
#Author : Divan Jagers
#Student no: JGRDIV001
#Date : 4/03/2014
hour= eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if 0<=hour<=23 and 0<=minutes<=59 and 0<=seconds<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")