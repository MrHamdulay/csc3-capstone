"""Program to categorize marks
Sithasibanzi Kondleka
24 April 2014"""

marks = input("Enter a space-separated list of marks:\n")
mark = marks.split(" ")
#print(mark)

#assigning variables to print the axes
a = "1 |"
b = "2+|"
c = "2-|" 
d = "3 |"
e = "F |"

for i in mark: #categorizing the marks
    if eval(i)>=75:
        a = a + "X"
    elif eval(i)>=70:
        b = b + "X"
    elif eval(i)>=60:
        c = c + "X"
    elif eval(i)>=50:
        d = d + "X"
    elif eval(i)<50:
        e = e + "X"
        
print(a)
print(b)
print(c)
print(d)
print(e)