"""Program to print list without duplicates
By Tinashe Choga
4/28/2014"""
# getting the input
string=input("Enter strings (end with DONE):\n")
list=[]
while string !="DONE" :
    #checking if word does not already exist in list
    if not string in list:
        list.append(string)
    string=input('')
print("")
print("Unique list:")
#printing the list without repetition
for i in list:
    print(i)