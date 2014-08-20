# A program that returns a list of input strings without duplicates
# Martin Batek
# 30 April 2014

print("Enter strings (end with DONE):")
x = ""
strings = []

while x != "DONE":
    x = input("")
    if x not in strings and x != "DONE":
        strings.append(x)
print()
print("Unique list:")
for word in strings:
    print(word)