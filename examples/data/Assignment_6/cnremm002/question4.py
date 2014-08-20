"""Grade
Emmanuel Conradie
25 April 2014"""

#marks input
mark = []
marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(" ")

fail = 0
third = 0
second1 = 0
second2 = 0
first = 0
#sort marks into catagories
for i in marks:
    if int(i) < 50:
        fail += 1
    elif int(i) >=50 and int(i) < 60:
        third += 1
    elif int(i) >=60 and int(i) < 70:
        second1 += 1
    elif int(i) >=70 and int(i) < 75:
        second2 += 1
    elif int(i) >= 75:
        first += 1

#print results
print ("1 |" + "X"*first)
print ("2+|" + "X"*second2)
print ("2-|" + "X"*second1)
print ("3 |" + "X"*third)
print ("F |" + "X"*fail)