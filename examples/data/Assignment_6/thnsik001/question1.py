"""Sikhulile Thenjwayo
  Assignment 6
  23 April 2014"""

#making list
string_list = []
length =0
count =0
#user enters list items
entry =""
print("Enter strings (end with DONE):")
while True:
    entry = input("")
    if entry == "DONE":
        break
    string_list.append(entry)
    if len(string_list[count])>length:
        length = len(string_list[count])
    count+=1
#print list
print("\nRight-aligned list:")
for i in range(count):
    print(" "*(length - len(string_list[i])),string_list[i],sep="")
    