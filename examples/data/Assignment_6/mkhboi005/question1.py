"""Tumi Mkhawana
22 April 2014
Assignment 6"""

strings= input("Enter strings (end with DONE):\n")
strings_list=[]

while strings!= "DONE":
    strings_list.append(strings)
    strings=input("")

maximum=[""]
for i in strings_list:
    if len(i) > len(maximum):
        maximum=i
print("")
print("Right-aligned list:")

for i in strings_list:
    print(" "* (len(maximum)-len(i)),i,sep="")