message = input("Enter strings (end with DONE):\n")
message.lower()
names = []
names.append(message)
while message != "DONE":
    message = input("")
    names.append(message)
names.remove("DONE")

num = []
print()
print("Right-aligned list:")
for name in names:
    length = len(name)
    num.append(length)
num.sort()
for name_1 in names:
    if len(name_1) <= num[-1]:
        print(" "*(num[-1]-len(name_1)) + name_1)