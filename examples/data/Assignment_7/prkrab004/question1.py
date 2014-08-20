#Assignment 7
#Question 1
#Rabia Parker
#PRKRAB004
#Due Date: 02/05/14

def no_duplicates():
    List=[] #create list
    sentence=input("Enter strings (end with DONE):\n")
    List.append(sentence)
    while sentence != 'DONE': #sentinel loop
        sentence=input()
        List.append(sentence)
        
        
    uniqueList=[] #unique list created
    for i in List:
        if i not in uniqueList:
            uniqueList.append(i)
     
    print()   
    print("Unique list:")
    for j in range(len(uniqueList)-1):
        print(uniqueList[j])
           
        
no_duplicates()
