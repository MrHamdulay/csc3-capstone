lst = []
words = input("Enter strings (end with DONE):\n") 
lst.append(words)
while words != "DONE":
    words = input()
    lst.append(words)
    
for a in lst:
    if a == "DONE":
        lst.remove(a) 

lst.reverse()
for x in lst:
    if x in lst[lst.index(x)+1:]:
        for j in lst[lst.index(x)+1:]:
            if j == x:
                lst.remove((j)) 

lst.reverse()

print("\nUnique list:")
for n in lst:
    print(n)
    