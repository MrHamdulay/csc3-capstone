### Tashiv Sewpersad (SWPTAS001)
### Assignment 6 - Question 1
### 2014 - 04 - 20

## Live Code
# Initialise Variables
aNames = []
iMaxLen = 0
# Get input
sName = input("Enter strings (end with DONE):\n")
while sName.upper() != "DONE":
	iLen = len(sName)
	if iLen > iMaxLen:
		iMaxLen = iLen
	aNames.append(sName)
	sName = input("")
# Generate Output
Output = "{0:>" + str(iMaxLen) + "}"
print("\nRight-aligned list:")
for Name in aNames:
	print(Output.format(Name))