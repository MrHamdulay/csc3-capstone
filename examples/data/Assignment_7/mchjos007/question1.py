#code to allow a user to input a list of strings and then prints them without any duplicates Joshua Michelson /29/04/2014#
list1 = []
usersays = input("Enter strings (end with DONE):\n")
while usersays != "DONE":
    list1.append(usersays)
    usersays=input()
print()
print("Unique list:")
for a in range (len(list1)):
    if list1[a] not in list1[0:a]:
        print(list1[a])