#Assignment 6 Question 1
#19 April 2014
#Alexi Kalamoudacos, right justified names list

x=[] #Initialising list
y=input('Enter strings (end with DONE):\n')
#Add names to list
while y!='DONE':
    x.append(y)
    y=input('')
#Find the longest name
JustifyLength=0
for i in range(len(x)):
    if len(x[i])>JustifyLength:
        JustifyLength=len(x[i])
print()
print('Right-aligned list:')
for j in x:
    print(j.rjust(JustifyLength))