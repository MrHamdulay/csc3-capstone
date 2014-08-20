#print input right aligned to longest string
#Aniq Hartle
#25/04/2014

print("Enter strings (end with DONE):")

#initialise variables
str_list = []
i = str
longest = 0

#take in input and add to array
#keep track of length of longest string
while i != "DONE":
    i = input()
    str_list.append(i)
    if len(i)>longest:
        longest =len(i)
        
print("\nRight-aligned list:")

#print output        
for j in range(len(str_list)-1):
    s = str_list[j]
    f = ("{0:>"+str(longest)+"}").format(s)
    print(f)