#question_2.py
#26_February_2014
#Asil_Motala
#MTLASI002

a=eval(input("Enter the hours:\n"))
b=eval(input("Enter the minutes:\n"))
c=eval(input("Enter the seconds:\n"))

if 0<=a<24 and  0<=b<60 and 0<=c<60:
    print("Your time is valid.")
else: print("Your time is invalid.")