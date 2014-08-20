#Question4
#Richard van Gysen
#22 April 2014

#get marks
x = input("Enter a space-separated list of marks:\n")
#split them
marks = x.split(" ")
a =0
b =0
c =0
d= 0
e = 0
#evaluate and class them
for mark in marks:
    if eval(mark) < 50:
        e+= 1
    elif 50 <=eval(mark) < 60:
        d+= 1
    elif 60 <= eval(mark)< 70:
        c+= 1
    elif 70 <= eval(mark) < 75:
        b+= 1
    elif eval(mark)>=75:
        a+= 1

#print each class with the counter
print("1 |"+'X'*a)
print("2+|"+'X'*b)
print("2-|"+'X'*c)
print("3 |"+'X'*d)
print("F |"+'X'*e)
    