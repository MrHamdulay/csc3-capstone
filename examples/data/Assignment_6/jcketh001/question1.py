#Program to right-align a list of strings entered by the user
#Ethan Jackson  
#21 April 2014

print("Enter strings (end with DONE):")
enter = ""#make empty string so can enter loop
lis = []
while enter !="DONE":#sentinel loop with "DONE" as sentinel
    enter = input("")
    lis.append(enter)
    continue       
#lis.append[enter]
lis.remove("DONE")#removes "DONE" from the list
count = 0
for item in lis:#runs through list
    if (len(item) > count):#measures length of each item in list and checks if it is greater than 0
        count = len(item)#if > 0 then it becomes max, and so on...
print("\nRight-aligned list:")
for item in lis:
    print((count-len(item))*" " + item)
