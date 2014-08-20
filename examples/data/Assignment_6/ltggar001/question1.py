'''Alligns all text to the right as far as the longest word is.
Gareth Lategan
22-04-2014'''

list1=[] #This is where the input is stored as items
list2=[] #This list has the length of each item in list1 instead of the word
print("Enter strings (end with DONE):")
a=input()
while a != "DONE": #Program only stops gathering input when this sentinal word is entered
    list1.append(a) #Adds each instance of input as a consecutive item in list1
    a=input() #Re-asks for new input
for b in range(len(list1)):
    list2.append(len(list1[b])) #Makes the length of each consecutive item in list1 correspond with the same item place as list 2

c=0 #Counter
max=0 #'max' represents the length of the longest word

while (c)<len(list2): #Makes sure the loop will stop when it reaches the last item in the list
    if list2[c] > max: #Makes sure the maximum value is extraced from the list and assigned to the variable 'e'
        max=list2[c]
    c+=1 #Continues the counter
print("\nRight-aligned list:")
f=0 #Used as both a counter and an item-position finder
while f < len(list1): #Makes sure the loop will stop when it reaches the last item in the list
    print((max-list2[f])*" ",list1[f],sep="") #The first part takes the difference in value from the longest word and the current word and prints that many spaces to compensate, then the word is printed with no space seperating the word and the compensating space
    f+=1 #Continues the counter