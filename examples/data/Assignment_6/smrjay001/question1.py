"""
Assignment 6 - Qiestion 1
Reproduce a list of strings with right allignment based on the lengh of the longest string.
Jayan Smart
April 2014
"""

#Initial Variables and Parameters:
repeat = True
list_names = []
leng = 0
longest = ""

#input list of strings until DONE is entered
print("Enter strings (end with DONE):")
while repeat == True:
    name = input()
    if name == 'DONE':
        repeat = False
    else:
        list_names.append(name)
       
#calculate longest string

for i in range(len(list_names)):
    temp = list_names[i]
    if leng < len(temp):
        leng = len(temp)
        longest = temp
        
#Add spaces to front of shorter words to create right allignment
print()
print("Right-aligned list:")
for j in range(len(list_names)):
    word = list_names[j]
    space = leng - len(word)
    print(space*' ',word, sep='')
    
