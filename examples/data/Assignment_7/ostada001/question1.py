'''Takes in a list of words and returns a list without doubles
Adam Oosthuizen
27th April 2014'''

names =[]


wordList = input("Enter strings (end with DONE):\n")

while wordList != "DONE":
    names.append(wordList)
    wordList = input()

print()
for i in range(0,len(names)-1):
    for j in range(i+1,len(names)):
            if names[i] == names[j] and names[i] != '' and names[j] !='':
                names[j] =''
                
               
          
print("Unique list:")
for i in range (len(names)):
    if names[i] != '':
        print(names[i])