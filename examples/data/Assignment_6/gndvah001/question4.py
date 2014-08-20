"""classify marks and draw histogram
Vahin Gounden
22-04-2014"""

#create list
marks = input("Enter a space-separated list of marks:\n")
mrklst = marks.split()

#create mark "holders"
q = 0
w = 0
e = 0
r = 0
t = 0

#classify marks
for i in mrklst:
    i = eval(i)
    if i < 50:
        q += 1
    elif i < 60:
        w += 1
    elif i < 70:
        e += 1
    elif i < 75:
        r += 1
    elif i >= 75:
        t += 1

#draw histogram
print("1 |",t*"X",sep = "")
print("2+|",r*"X",sep = "")
print("2-|",e*"X",sep = "")
print("3 |",w*"X",sep = "")
print("F |",q*"X",sep = "")