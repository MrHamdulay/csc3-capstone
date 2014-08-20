"""Sikhulile Thenjwayo
  Assignment 6
  23 April 2014"""

#user enters marks
marks = (input("Enter a space-separated list of marks:\n")).split()
histbars = ["","","","",""]
for i in range(len(marks)):
 marks[i] = eval(marks[i])
 if marks[i]<50:
  histbars[4] +=  "X"
 elif marks[i]<60:
  histbars[3] += "X"
 elif marks[i]<70:
  histbars[2] += "X" 
 elif marks[i]<75:
  histbars[1] += "X"
 else:
  histbars[0] += "X" 

print("1 |",histbars[0],sep="")
print("2+|",histbars[1],sep="")
print("2-|",histbars[2],sep="")
print("3 |",histbars[3],sep="")
print("F |",histbars[4],sep="")
