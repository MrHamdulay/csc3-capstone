#ASSIGNMENT_4
#QUESTION_2
#ASIL_MOTALA
#MTLASI002
x=eval(input("Enter the height of the triangle:\n"))
for i in range(1,2*x,2):
    print(" "*((2*x-1-i)//2),end="")
    print("*"*i)