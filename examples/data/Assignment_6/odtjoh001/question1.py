"""Program to print out a right-aligned lis of strings
John Odetokun ODTJOH001
20 April 2014"""
#create list
list = []
print("Enter strings (end with DONE):\n")
name = input()
#assign strings to array
while name != "DONE":
    list.append(name)
    name = input()

print("Right-aligned list:")

longest = 0
#finding longest word
for j in range(len(list)):
    if len(list[j]) > longest:
        longest = len(list[j])
#printing list
for i in range(len(list)):
    print("{0:>{1}}".format(list[i], longest))