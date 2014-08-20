"""Assignment 6 Question 1
19 April 2014
Jordan Kadish, right justified names list"""

Name=[] #Initialising list
NamesInput=input('Enter strings (end with DONE):\n')
#Add names to list
while NamesInput!='DONE':
    Name.append(NamesInput)
    NamesInput=input('')
#Find the longest name
JustifyLength=0
for i in range(len(Name)):
    if len(Name[i])>JustifyLength:
        JustifyLength=len(Name[i])
print()
print('Right-aligned list:')
for j in Name:
    print(j.rjust(JustifyLength))