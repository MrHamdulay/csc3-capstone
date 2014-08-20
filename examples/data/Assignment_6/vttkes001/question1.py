"""User enter strings
Keshin Vittee
21 April 2014"""

print("Enter strings (end with DONE):\n")
x = []
while True:
    userin = input("")
    if userin == 'DONE':
        break
    else:
      x.append(userin)
      

print("Right-aligned list:")
longstr = 0

for i in range(len(x)):
    if len(x[i]) > longstr:
        longstr = len(x[i])

for a in x:
    print(a.rjust(longstr))
    