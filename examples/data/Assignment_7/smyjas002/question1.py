#Jason Smythe
#assignment 7
#question 1
stringList = []

def scrubDuplicates(stringList):
	scrubedList = []
	for i in stringList:
		if i in scrubedList:
			pass
		else:
			print(i)
			scrubedList.append(i)
			
stringList.append(input("Enter strings (end with DONE):\n"))
while stringList[-1] != "DONE":
    stringList.append(input())
stringList.pop()

print("\nUnique list:")

scrubDuplicates(stringList)

'''
 Write a Python program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.

Use the sentinel "DONE" to end the input list.

Sample I/O:

Enter strings (end with DONE):
the
old
man
and
the
sea
DONE

Unique list:
the
old
man
and
sea
'''
