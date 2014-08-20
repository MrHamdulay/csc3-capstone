a = False
print("Enter strings (end with DONE):\n")
list = []
while a == False:
    temp = input()
    if temp == 'DONE':
            break
    if list.count(temp) == 0:
        list.append(temp)
print("Unique list:")
for i in range(len(list)):
    print(list[i])