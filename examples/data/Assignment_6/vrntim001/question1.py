''' Right alligned strings
Timothy Mostert
23/04/14'''

the_list = []
string = ""

print("Enter strings (end with DONE):")
while True:
    string = input()
    if string == "DONE":
        break
    the_list.append(string)

width = 0
    
for i in the_list:
    a = len(str(i))
    if a > width:
        width = a

    
print()
print("Right-aligned list:")
for i in the_list:
    right = '{0:>'+str(width)+'}'
    print(right.format(i))
    
    
    
