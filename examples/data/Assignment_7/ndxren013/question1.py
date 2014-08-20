x = []
x.append(input("Enter strings (end with DONE):\n"))
count = 1
y = " "

if x[0] == 'DONE':
        x.pop()
        count -= 1
        y = 'DONE'

while y != "DONE" :
    y = input()
    
    if y == "DONE" :

        break
    
    elif y in x :

        continue
        
    else :

        x.append(y)
        count += 1
print()
print("Unique list:")

for i in range (count) :

    print(x[i])
