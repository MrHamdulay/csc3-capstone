hour = eval(input('Enter the hours:\n'))
minute = eval(input('Enter the minutes:\n'))
second = eval(input('Enter the seconds:\n'))

#FI check against non int input, ie floats but also against input such as strings in a friendly way
if (hour < 24 and hour >= 0 and minute >= 0 and minute < 60 and second >= 0 and second < 60):
	print("Your time is valid.")
else:
	print("Your time is invalid.")
	
	
'''
 Sample I/O

Enter the hours:
21
Enter the minutes:
7
Enter the seconds:
7
Your time is valid.

Sample I/O

Enter the hours:
25
Enter the minutes:
-7
Enter the seconds:
0
Your time is invalid.

Sample I/O

Enter the hours:
21
Enter the minutes:
7
Enter the seconds:
72
Your time is invalid.
'''
