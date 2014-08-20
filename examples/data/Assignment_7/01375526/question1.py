l = []
d = {}

s = input ("Enter strings (end with DONE):\n")
while s!="DONE":
    if not s in d:
       d[s] = 1 
       l.append (s)
    s = input ("")

print ("\nUnique list:")
for item in l:
    print (item)
    