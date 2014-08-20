# assignment 7 question 1
strings = []
print("Enter strings (end with DONE):")
text = ""
while text != "DONE":
    text = input()
    if text != "DONE":
        strings.append(text)
print("\nUnique list:")
for i in range(len(strings)):
    unique = True
    count = 0
    for j in range(i, -1, -1):
        if strings[i] == strings[j]:
            count+=1
    if count==1:
        print(strings[i])