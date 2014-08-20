"""Assignment 6, question 4
JT
23-04-2014"""

#create lists for 5 catagories
list1 = []
list_up2 = []
list_low2 = []
list3 = []
listF = []

#get list of marks from user and convert to a list
def get_list():
    string = input("Enter a space-separated list of marks:\n")
    allmarks = string.split(" ")
    return allmarks

#sort list of all marks into catagory lists
def sort():
    for i in get_list():
        if i.isdigit():
            i = eval(i)
            if 0 <= i < 50:
                listF.append(i)
            elif i < 60:
                list3.append(i)
            elif i < 70:
                list_low2.append(i)
            elif i < 75:
                list_up2.append(i)
            elif i <= 100:
                list1.append(i)

#print graph
def graph():
    sort()
    print("1 |","X"*len(list1),sep='')
    print("2+|","X"*len(list_up2),sep='')
    print("2-|","X"*len(list_low2),sep='')
    print("3 |","X"*len(list3),sep='')
    print("F |","X"*len(listF),sep='')
    
    
    
graph()