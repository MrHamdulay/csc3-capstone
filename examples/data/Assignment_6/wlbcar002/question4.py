"""histogram of marks
Carla Wilby
19 April 2014"""

#get marks and add to array
marks_in = input("Enter a space-separated list of marks:\n")
marks = marks_in.split(" ")

#sort marks into categories
sorted_marks = {"1 |":"", "2+|":"", "2-|":"", "3 |":"", "F |":""}
for i in marks:
    i = eval(i)
    if i < 50:
        sorted_marks['F |'] += "X"
    elif 50 <= i < 60:
        sorted_marks['3 |'] += "X"
    elif 60 <= i < 70:
        sorted_marks['2-|']  += "X"
    elif 70 <= i < 75:
        sorted_marks['2+|']  += "X"
    elif i >= 75:
        sorted_marks['1 |'] += "X"
    
#return histogram
print('1 |', sorted_marks['1 |'],sep="")
print('2+|', sorted_marks['2+|'],sep="")
print('2-|', sorted_marks['2-|'],sep="")
print('3 |', sorted_marks['3 |'],sep="")
print('F |', sorted_marks['F |'],sep="")
