# a programe to count the number of votes for each political party in an election
# mashau zwivhuya
# 21 april 2014
def main():
    # creating empty list
    list1=[]
    print("Independent Electoral Commission\n--------------------------------")
    names=input("Enter the names of parties (terminated by DONE):\n")
    count=0
    #adding names to list
    list1.append(names)
    list2=[]
    while names !="DONE":
        names=input("")
        #calculating occurances
        if names in list1:
            count+=count
        list1.append(names)
    # removing "DONE"    
    if list1[-1]=="DONE":
        list1.remove("DONE")
    # sorting the list    
    list1.sort()    
    print("")
    print("Vote counts:")
    # checking occurances and print formating
    for i in range(1):
        count=0
        for x in list1:
            count=list1.count(x)
            if x in list2:
                continue
            list2.append(x)
            print(x," "*(11-len(x)),"- ",count,sep="")
main()    