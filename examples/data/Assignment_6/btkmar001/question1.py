# question1.py
# a progam which aligns all given names to the right
# Martin Batek
# BTKMAR001
# 22 April 2014

l = []
x= ""
print("Enter strings (end with DONE):")
while x != "DONE":
    x = input("")
    if x != "DONE":
        l.append(x) # Creates a list of strings
print()
maxlen = 0
for name in l:
    if len(name)>maxlen:
        maxlen = len(name) # Finds the longest string
        
print("Right-aligned list:")        
for name in l:
    print(((maxlen-len(name))*" ")+name)  