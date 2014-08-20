"""Program to print out a list of strings right aligned (Question 1)
24 April 2014
Jaren Hendricks"""

# Prints heading and empty lists
print("Enter strings (end with DONE):")
strings = []
arrNum = []
x=''

# Gets and adds strings to list until input equals 'DONE'
while True:
    x = input()
    if x == 'DONE':
        break
    else:
        wrds = strings.append(x)

# Gets the longest string value
    for i in range(len(strings)):   
        length = len(strings[i])
        num = arrNum.append(length)
    maxi = max(arrNum)
# Prints the headings
print()
print('Right-aligned list:')

# outputs the strings Right-aligned
for j in strings:
    print(j.rjust(maxi))
    
 