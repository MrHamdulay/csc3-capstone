"""Dzunisani Nyoni
27 April 2014
A program to print a unique list of strings entered by user"""

def string():
	
	stringlist=[]		#initializing a list
	string=input("Enter strings (end with DONE):\n")
	stringlist.append(string) 	#Add items to the list
	new_list=[]
	counter={}
	
	if string=="DONE":
		pass
	else:
		
		while string != "DONE":		#iterates when DONE is not entered
			string = input()
			
			if string == "DONE":
				pass
			else:
				
				stringlist.append(string)
				
		for i in stringlist:
			if i not in new_list:
				new_list.append(i)
	print()
	print("Unique list:")		
	for i in new_list:
		print(i)
		
string()