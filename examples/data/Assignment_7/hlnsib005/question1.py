"""Name: Sibulele Hlongwane
   Date" 27 April 2014
   Assigment: Output a list without duplicates in the same order"""
names=[]
icount=0
#Prompts user to enter strings
name= input("Enter strings (end with DONE):\n")
#Re-Iterates until user has enter DONE
while name!= "DONE":
            names.append(name)
            name=input()
#reverses names so that in the end the first word which appears in list displays in correct order 
names.reverse()
#loops at each name in the array
for a in names:
            #counts the number of times words is in array
            num=names.count(a)
            #loop which re-iterates for the number that the names appears-1
            for j in range(num):
                        #if name count is greater than 1 then remove the name
                        if names.count(a)>1:
                                    names.remove(a)
#reverses names back into original form to disply names in order                               
names.reverse()
print("\nUnique list:")
#displays names
for a in names:
            print(a)

