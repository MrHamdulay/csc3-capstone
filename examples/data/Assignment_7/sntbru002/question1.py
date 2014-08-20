"""the programe that eliminates the duplicate
By Bruce Sontshoto
29 April 2014"""
#let = {}
name = []
stri = input("Enter strings (end with DONE):\n")
while True:
    if stri == "DONE":
        break
    elif ((stri in name) == False):
        name.append(stri)
    
    stri = input("")
print()
print("Unique list:")
    
for i in range(len(name)):
    print(name[i])
   
        