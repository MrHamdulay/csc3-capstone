#Jason Smythe
#assignment 6
#question 1
nameList = []

def longestWordLen(nameList):
	length = 0
	#print("longest word function")
	for i in nameList:
		#print("Word:", i)
		if length < len(i):
			length = len(i)
			#print("length Change:", length)
	return length

def rightAlign(nameList, numCharactors):
    for i in nameList:
        space = numCharactors - len(i)
        string = " "*space 
        string += i
        print(string)

nameList.append(input("Enter strings (end with DONE):\n"))
while nameList[-1] != "DONE":
    nameList.append(input())
nameList.pop()

print()

longestWord = longestWordLen(nameList)
#print(longestWord)
print("Right-aligned list:")
rightAlign(nameList, longestWord)



