#Kovlin Perumal
#PRMKOV001
#30/04/2014
#Question 1 - Unique Strings

string = input("Enter strings (end with DONE):\n")
strings = [] 
while not string == 'DONE' :
    if string in strings :
        string = input()
        continue
    else:
        strings.append(string)
    
    string = input()
print()   
print("Unique list:")    

for a in strings :
    print(a)