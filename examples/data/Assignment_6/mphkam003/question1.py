"""print out a list right-aligned with the longest string
Kamogelo Mphela
20 April 2014"""

#create the list
string = []
x = input("Enter strings (end with DONE):\n")
while x != "DONE":
    string.append(x)
    x = input("")
    
#determine the longest string
m = 0
for n in string:
    count = len(n)
    if  count> m:
        m = count


# print out the list right-aligned with the longest string
print()
print("Right-aligned list:")
for x in string:
    print(" "*(m-len(x)),x,sep="")