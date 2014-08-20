"""prints out a list of strings right aligned with the longest string"""

strings = []
x = "" 
max_length = 0

# get strings and longest string length
print("Enter strings (end with DONE):\n")
while x != "DONE":
    x = input()
    if len(x) > max_length:
        max_length = len(x)
    if x != "DONE":
        strings.append(x)

# output
print("Right-aligned list:")
for i in strings:
    print(" " * (max_length - len(i)), end = "")
    print(i)
    
    
    