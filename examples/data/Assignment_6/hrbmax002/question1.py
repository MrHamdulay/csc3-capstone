print ("Enter strings (end with DONE):")
inp = ""
list1 = []
sentinel = "DONE"
while inp != sentinel:
    inp = input()
    list1.append(inp)

max_letter = 0

for i in range (len(list1)-1):
    if len(list1[i])>max_letter:
        max_letter = len(list1[i])

print ("\nRight-aligned list:")

for j in range (len(list1)-1):
    print (" "*(max_letter-len(list1[j]))+list1[j])
