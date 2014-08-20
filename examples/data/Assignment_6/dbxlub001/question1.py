"""Right Alligned list
Lubalethu Dube
23 April 2014"""
def Mr_List():
    the_list=[]
    i=input("Enter strings (end with DONE):\n")
    while i!= "DONE" and i!="done":
        the_list.append(i)
        i=input("")
    #right aligne the list
    #find longest
    longy=0
    for j in range (len(the_list)):
        if len(the_list[j])>longy:
            longy=len(the_list[j])
            
    #print in ryt alynd
    print("\nRight-aligned list:")
    for knee in range(len(the_list)):
        print(("{0:>"+str(longy)+"}").format(the_list[knee]))
            

Mr_List()