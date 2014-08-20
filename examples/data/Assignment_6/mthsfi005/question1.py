'''program to align strings to the right
Sfiso Mthembu MTHSFI005
04/20/2014'''

#ask for strings and stores them as a list
words = input("Enter strings (end with DONE):\n")

list = []

#add every input to list
while words!="DONE":
    list.append(words)
    words=input("")
#make second list for lengths of each string
list2=[]

#add every length to length list 
for i in list:
    list2.append(len(i))

#Give output
print('')
print("Right-aligned list:")
for i in list:
    print(" " * (max(list2)-len(i)) + i)