"""program to count marks
Paul Truter
25 April 2014"""

#get list of marks
mark = input("Enter a space-separated list of marks:\n")
#split list
marks = mark.split(" ")

#sort list
marks.sort()


#create new list then check for code
code=[]
for i in marks:
    if int(i) >= 75:
        code.append("1")
    elif int(i) >= 70:
        code.append("2+")
    elif int(i) >= 60:
        code.append("2-")
    elif int(i) >= 50:
        code.append("3")
    elif int(i) >= 0:
        code.append("F")
    else:
        break

#create histogram
print("1 |"+code.count("1")*"X")
print("2+|"+code.count("2+")*"X")
print("2-|"+code.count("2-")*"X")
print("3 |"+code.count("3")*"X")
print("F |"+code.count("F")*"X")