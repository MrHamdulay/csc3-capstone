### Tashiv Sewpersad (SWPTAS001)
### Assignment 6 - Question 4
### 2014 - 04 - 20

## Constants
CategoryTops = [50,60,70,75,101] # Top end % of each category
CategoryTitles = ["F ","3 ","2-","2+","1 "] # Category Headings

## Declarations
def ExtractNumbers(StrVals):
	__doc__ = "A function that outputs a integers in list form from strings in list form"
	result = []
	for i in StrVals:
		iInt = int(i)
		result.append(iInt)
	return result	

## Live Code
# initialisr variables
aMarks = []
aBars = [0,0,0,0,0]
# Get input
aMarks = ExtractNumbers(input("Enter a space-separated list of marks:\n").split())
# Count number of bars per category
for i in aMarks:
	for j in range(5):
		if i < CategoryTops[j]:
			aBars[j] += 1
			break
# Print nice output
for i in range(4,-1,-1):
	LineBar = "X"*aBars[i]
	print(CategoryTitles[i],LineBar,sep="|")
