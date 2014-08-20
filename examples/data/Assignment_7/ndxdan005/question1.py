words=[]
print("Enter strings (end with DONE):")
word=input()
while word!="DONE":
    words.append(word)
    word=input()
seen=[]
new_list=[]
for element in words:
    if element in seen:
        continue
    else:
        if element in new_list:
            continue
        else:
            new_list.append(element)
print()
print("Unique list:")
for element in new_list:
    print(element)
    