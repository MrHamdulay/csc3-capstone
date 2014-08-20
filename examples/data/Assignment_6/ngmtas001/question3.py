#NGMTAS001
#Tase Ngambi
#Question 3
#20 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
names =[]
entered = ""
print("Enter the names of parties (terminated by DONE):\n")

def count(self):

    output = {}
    for each in self:
        if not each in output:
            output[each] = 0
        output[each]+=1
    return output  



#loops until done is entered
while entered != "DONE":
    entered = input()
    if entered != 'DONE':
        names.append(entered)

outputList = count(sorted(names))

print("Vote counts:")

for x in sorted(outputList):
    print(x, " "*(10-len(x))," - ",outputList[x], sep ="")
    
print()    