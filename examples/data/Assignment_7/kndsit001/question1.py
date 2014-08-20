"""Program to print a list without duplicates
Sithasibanzi Kondleka
01 May 2014"""

strings = []
string = input("Enter strings (end with DONE):\n")
while string != "DONE":
    if string in strings:
        string = input("")
        continue
    else:
        strings.append(string) #keep adding to the list
        string = input("")
print()
print("Unique list:")
for string in strings:
    print(string)