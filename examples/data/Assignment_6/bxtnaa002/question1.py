# question1.py
# author: bxtnaa002


# create a list as user inputs names
names = [] 
name = input("Enter strings (end with DONE):\n")
while name != "DONE": # list continues to extend until user inputs done
        names.append(name)
        name = input("")

print("\nRight-aligned list:")  

if names != []:
        max_length = max(len(i) for i in names) # calculate the maximum length which is the longest names in the list of names
        
        for name in names:
                print('{0:>{1}}'.format(name, max_length)) #using format to right-aligned the list of names by using maximum length

