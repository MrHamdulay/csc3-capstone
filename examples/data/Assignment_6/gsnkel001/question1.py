#2014/04/23
#Right aligned list
#Kelly Goosen

print("Enter strings (end with DONE):") 

names=[] #empty string
name1=""
name1 = input() #getting input from user
max_length = 0 #initiate variable
while name1 != 'DONE':
       if len(name1)>max_length: #finding length of longest word in list
              max_length=len(name1)
       names.append(name1) #adding names to list
       name1 = input()
       
print()

print("Right-aligned list:")

for i in (names):
       print(i.rjust(max_length)) #adjusting list to right allignment