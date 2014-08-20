""""Assignment 6 question 4: 
Ailsa Mackay MCKAIL001
2014-04-22"""

M = input("Enter a space-separated list of marks:\n")
marks_str = M.split()
marks_int = [int(i) for i in marks_str]
    
first = 0
u_second = 0
l_second = 0
third = 0
fail = 0
for i in marks_int:
    if i >= 75:
        first+=1
    elif i >= 70:
        u_second+=1
    elif i >= 60:
        l_second+=1
    elif i >= 50:
        third+=1
    else:
        fail+=1
    
print("1 |", "X"*first, sep="")
print("2+|", "X"*u_second, sep="")
print("2-|", "X"*l_second, sep="")
print("3 |", "X"*third, sep="")
print("F |", "X"*fail, sep="")




    