
#Shivam Ragoonaden
#Histogram of mark categories at UCTS

marks = input("Enter a space-separated list of marks:\n")
marklist = []  #Create an array for the marks

categories = ["1 ","2+","2-","3 ","F "] #Initialise categories
categoriesCount = [0,0,0,0,0]
    #Initialise the category counts


for mark in marks.split():  #Get the marks one-by-one 
    mark = int(mark)
    marklist.append(mark)  #Add the mark to array marks

for i in range(len(marklist)):
    if marklist[i] >= 75:
        categoriesCount[0] += 1
    elif marklist[i] >= 70:   #Check the marks one-by-one and increment the appropriate category   
        categoriesCount[1] += 1
    elif marklist[i] >= 60:
        categoriesCount[2] += 1 
    elif marklist[i] >= 50:
        categoriesCount[3] += 1  
    else:
        categoriesCount[4] += 1
   
for i in range(len(categories)):
    print(categories[i] + "|" + "X"*categoriesCount[i])  #Print the categories and their counts one-by-one
