# a programe where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.
# mashau zwivhuya
# 21 april 2014
def main():
    #creating list
    list1=[]
    #getting input from user
    names=input("Enter strings (end with DONE):\n")
    #calculating length of names
    length_first=len(names)
    length=0
    #adding names to list
    list1.append(names)
    # adding to list and evaluating length
    while names !="DONE":
        names=input("")
        list1.append(names)
        if len(names)>length:
            length=len(names)
    # changing the value of length
    if length>length_first:
        length_first=length
    #removing "DONE" from list    
    if list1[-1]=="DONE":
        list1.remove("DONE")
    print()    
    print("Right-aligned list:")    
    for i in list1:
        print(" "*(length_first-len(i)),i,sep="")     
        
main()    