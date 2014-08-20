"""enter a list of strings then print them in same order without duplicates
Lauren Denny
29 April 2014"""

print("Enter strings (end with DONE):") #ask for strings
List=[]

while True:
    string=input()                      #get string
    if string=="DONE":                  #stop getting strings if inputted string is "DONE"
        break
    elif string in List:                #if string already in list, do nothing then ask for a new string
        continue
    else:
        List.append(string)             #if string not in list, add it to the end of the list

print()
print("Unique list:")

for string in List:                     #print each string in the list on a new line (in the order they appear in the list)
    print(string)
        