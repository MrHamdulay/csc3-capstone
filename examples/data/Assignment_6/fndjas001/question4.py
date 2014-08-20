"""A program that takes a list of marks and creates a histogram of them
Jason Findlay
25/04/2014"""

marks_lst=[]
first=0
u_second=0
l_second=0
third=0
fail=0

mark=input("Enter a space-separated list of marks:\n")

marks_lst=mark.split(" ")
for i in range(len(marks_lst)):
    marks_lst[i]=int(marks_lst[i])

for i in range(len(marks_lst)):
    if marks_lst[i]>=75:
        first+=1
    elif marks_lst[i]>=70:
        u_second+=1
    elif marks_lst[i]>=60:
        l_second+=1
    elif marks_lst[i]>=50:
        third+=1
    elif marks_lst[i]<50:
        fail+=1

print("1 |"+"X"*first)
print("2+|"+"X"*u_second)
print("2-|"+"X"*l_second)
print("3 |"+"X"*third)
print("F |"+"X"*fail)
