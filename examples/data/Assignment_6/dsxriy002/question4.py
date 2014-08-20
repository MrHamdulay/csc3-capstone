#Riya Desai
#Assignment 6, Question 4
#23 April 2014



listofmarks = input("Enter a space-separated list of marks:\n")
marks = listofmarks.split(" ")
#define marks

fail = 0
first = 0
third = 0
lowersecond = 0
uppersecond = 0

#check different marks
for i in marks:
    if 0 <= eval(i) < 50:
        fail = fail + 1
    elif 50 <= eval(i) < 60:
        third = third + 1
    elif 60 <= eval(i) < 70:
        lowersecond = lowersecond + 1
    elif 70 <= eval(i) < 75:
        uppersecond = uppersecond + 1
    elif eval(i) >= 75:
        first = first + 1
        
print("1 |"+ ("X" * first))
print("2+|"+ ("X" * uppersecond))
print("2-|"+ ("X" * lowersecond))
print("3 |"+ ("X" * third))
print("F |"+ ("X" * fail))