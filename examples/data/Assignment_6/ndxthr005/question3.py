"""thrianka naidoo
ndxthr005
assignment 6: question 3, a program to count multiples in an array"""

print("Independent Electoral Commission")   #print headings
print("--------------------------------")

fruits = []                                 #create list for all fruits
counters = {}

fruit = input("Enter the names of parties (terminated by DONE): \n") #input from user (votes)

while fruit != "DONE":                      #stops loop if fruit = done
    fruits.append(fruit)                    #adds fruit to list: fruits
    fruit = input("")                       #allows for further input 


for word in (fruits):                       #creates dictionary
    if not word in counters:
        counters[word] = 0
    counters[word]+=1                       #counts per occurance of letter

print()   
print("Vote counts:")
y = "{0:<10}"                               #format

for word in sorted(counters):               #outputting solution
    print(y.format(word),"-",counters[word])
