"""Program converting string to list with names in special allignment
Khanyisile Morudu
20 April 2014"""

#Write a Python program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.

n = " "
# initial input
string  = input("Enter strings (end with DONE):\n")
names = [] 

# creating the list
while string.upper() != "DONE":
  names.append(string)
  string = input("")

#getting max characters space needed
max_num = 0
for i in range(len(names)):
    if max_num < (len(names[i])):
        max_num = (len(names[i]))

#print in formatted string
a =  "{0:>" + str(max_num) + "}"
print("\nRight-aligned list:")
for i in range(len(names)):
  print(a.format(names[i]))
