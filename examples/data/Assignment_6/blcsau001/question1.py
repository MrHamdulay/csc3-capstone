#Code to display a list that is right-alligned
#Saul Bloch
#22 April 2014

Array = [] # creating array
names = input("Enter strings (end with DONE):\n")
#adding inputs to array until 'DONE' is inputted
while names != "DONE":
    Array.append(names)
    names = input()

length = ""
#getting longest word in array
for i in range(len(Array)):
    if len(length) < len(Array[i]):
        length = Array[i]
print()
#printing righ-alligned list
print("Right-aligned list:")
for i in range(len(Array)):
    
    if Array[i] == length:
        print(length)
    else : print(" "*(len(length)-len(Array[i]))+ Array[i])