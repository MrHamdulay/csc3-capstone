# danson masuka
#program to vote
#23 april 2014

print ("Independent Electoral Commission")
print ("--------------------------------")
#intial entry
names_input = input("Enter the names of parties (terminated by DONE):\n")
names = []

# looping to enter in list until DONE
while names_input != 'DONE':
    names.append(names_input)
    names_input = input ("")

print ()
counter = {}
for word in names:
    if not word in counter.keys():
        counter[word] = 1
    else:
        counter[word] += 1
print ("Vote counts:")
for word in sorted(counter):
    print (word," "*(10-len(word))+"-",counter[word])