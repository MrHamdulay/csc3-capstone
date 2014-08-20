def unique():
    z = True
    print("Enter strings (end with DONE):\n")
    list = []
    while z == True:
        string = input()
        if string == 'DONE':
            break
        if list.count(string) == 0:
            list.append(string)
    print("Unique list:")
    for i in range(len(list)):
        print(list[i])
unique()