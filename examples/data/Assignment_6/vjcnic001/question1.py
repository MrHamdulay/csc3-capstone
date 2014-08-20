'''input names and return list with right alignment
Nicol Vojacek'''
name_list = []
names = input("Enter strings (end with DONE):\n")
name_list.append(names) #add first input to list

while names != "DONE": 
	names = input()
	name_list.append(names) #add further input to list
	
for a in name_list:
	if a == 'DONE':
		name_list.remove(a) #remove DONE from list that kills while loop
	
max = 0
print()
print("Right-aligned list:")
for t in name_list: 
	for s in name_list:
		if len(s) > max: #find longest name for alignment
			max = len(s)
	print(" "*(max-len(t))+t) #align names to the right with regard to longest name