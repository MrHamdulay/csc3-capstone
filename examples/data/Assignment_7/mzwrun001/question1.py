"""Program to check duplicates in a list
Runako Muzwidzwa
30/04/2012"""
inpt=input("Enter strings (end with DONE):\n")
string=[]
while inpt!="DONE":
    string.append(inpt)
    inpt=input()
    
print()
print("Unique list:")

new_string=[]
for i in range(len(string)):
    if string[i] in  new_string:
        continue
    else:
        new_string.append(string[i])
        
for new_word in new_string:
    print(new_word)