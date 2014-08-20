#Tase Ngambi
#NGMTAS001
#Question1

print("Enter strings (end with DONE):")
words =[]
inputVal = ""
tmp= ""
while inputVal != 'DONE':
    inputVal = input()
    
    if tmp.find(inputVal) == -1 and inputVal != 'DONE':
        words.append(inputVal)
    
    tmp = tmp +" "+ inputVal

    
print("\nUnique list:")
for x in words:
    print (x)
    
    