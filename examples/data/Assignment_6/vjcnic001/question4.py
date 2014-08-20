'''Lists marks and returns histogram with mark spread
Nicol Vojacek'''
import collections
mark_list = []
count = []
first = 0
up_sec = 0
down_sec = 0
third = 0
fail = 0

marks = input("Enter a space-separated list of marks:\n")

for a in marks.split(" "):
	mark_list.append(a) #Separate marks into list
	
for x in mark_list:
	if eval(x)>=75:
		first = first + 1
	elif eval(x)>=70:
		up_sec = up_sec + 1
	elif eval(x)>=60:
		down_sec = down_sec +1
	elif eval(x) >=50:
		third = third + 1
	elif eval(x)<50:
		fail = fail + 1 #count how many marks fall within each subsection 

count.append(first)
count.append(up_sec)
count.append(down_sec)
count.append(third)
count.append(fail) #store mark counters for each subsection in list 

		
print("1 |"+count[0]*"X")
print("2+|"+count[1]*"X")
print("2-|"+count[2]*"X")
print("3 |"+count[3]*"X")
print("F |"+count[4]*"X") #return histogram 
