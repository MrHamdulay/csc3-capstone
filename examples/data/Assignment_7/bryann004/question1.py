# anna borysova
# ass7, q1
# 2014-04-30

print("Enter strings (end with DONE):")
strings = []
item = ""

while True:
    item = input()
    if item == "DONE":
        break
    else:
        strings.append(item)
    
unique_list = []
for word in strings:
    if not word in unique_list:
        unique_list.append(word)
        
print("\nUnique list:")
for word in unique_list:
    print(word)
    