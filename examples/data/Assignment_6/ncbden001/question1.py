#Program to right align a list
#Denzel Ncube
#22 April 2014



#Function to align words
def rightalign():
    maxi = 0
    newlst = []
    lst = []
    maxlst = []
    print("Enter strings (end with DONE):\n")
    word = ""
    #Adding to the different lists
    while word != "DONE":
        word = input()
        lst.append(word)
        maxlst.append(len(word))
    #Deleting "DONE"
    del lst[-1]
    #Getting the maximum length of any item in the list
    maxlst.sort()
    maxi = maxlst[len(maxlst)-1]
    #Formatting the list to be right aligned
    for k in range(len(lst)): 
        newlst.append((maxi-len(lst[k]))*" "+lst[k])
    #Displaying the aligned list
    print("Right-aligned list:")
    for l in range(len(newlst)):
            print(newlst[l])
    

main = rightalign()





     

