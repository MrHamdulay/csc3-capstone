"""program to print out the first occurrence of a string from an input list of strings
peter m muriuki"""

#get list of strings and store them in an array
name_str=input("Enter strings (end with DONE):\n")
strings=[]
while name_str!="DONE":
    strings.append(name_str)
    name_str=input("")
print ("\n"+"Unique list:")
b=0
for item in strings:
    a=strings.index(item)
    if a==b:
        print(strings[a]) #print only the first occurrence of string
    b+=1
