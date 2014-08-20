import math

input_file = input("Enter the marks filename:\n")
f = open(input_file,"r")

marks = []
names = []
sum = 0
count = 0
dev = 0 
advisor = ["List of students who need to see an advisor:"]
blah = 0

s = f.read().replace("\n",",")
names = s.split(",")

for n in names[1::2]:
	marks.append(n)
	names.remove(n)

for n in marks:
	sum = sum + int(n)
	count = count + 1

ave = sum/count 


for s in marks:
	blah = blah +((int(s) - int(ave))**2)

p = blah/count
dev = math.sqrt(p)


print("The average is:", format(ave,'.2f'))
print("The std deviation is:","{0:.2f}".format(dev))

for a in marks:
	if int(a) < (ave-dev):
		d = marks.index(a)
		advisor.append(names[d])

if len(advisor) > 1:
	for i in advisor:
		print(i)