dict = {}
print("Independent Electoral Commission")
print("--------------------------------")
x = input("Enter the names of parties (terminated by DONE):\n")
print("")
while x != 'DONE':
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
    x = input("")
    
print("Vote counts:")
for i in sorted(dict):
    print (('{0:<10} - {1:<10}').format(str(i), str(dict[i])))